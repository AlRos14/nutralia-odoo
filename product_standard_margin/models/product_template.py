# Copyright (C) 2012 - Today: Camptocamp SA
# @author: Joel Grand-Guillaume
# Copyright (C) 2019 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Column Section
    list_price_vat_excl = fields.Float(
        compute="_compute_margin",
        string="Sale Price VAT Excluded",
        digits="Product Price",
    )

    standard_margin = fields.Float(
        compute="_compute_margin",
        string="Margin",
        digits="Product Price",
        help="Margin is [ sale price (Wo Tax) - cost price ] "
        "of the product form (not based on historical values). "
        "Take care of tax include and exclude. If no sale price, "
        "the margin will be negativ.",
    )

    standard_margin_rate = fields.Float(
        compute="_compute_margin",
        string="Margin (%)",
        digits="Product Price",
        help="Margin rate is [ Margin / sale price (Wo Tax) ] "
        "of the product form (not based on historical values)."
        "Take care of tax include and exclude.. If no sale price "
        "set, will display 999.0",
    )
    standard_markup_rate = fields.Float(
        compute="_compute_margin",
        string="Markup (%)",
        digits="Product Price",
        help="Markup rate is [ Margin / cost price (Wo Tax) ] "
        "of the product form (not based on historical values)."
        "Take care of tax include and exclude.. If no cost price "
        "set, will display 999.0",
    )

    final_cost = fields.Float(
        'Final cost', compute='_compute_final_cost',
        inverse='_set_final_cost', search='_search_final_cost',
        digits='Product Price', groups="base.group_user",
        help="""Same behavior that standard_price. It's works as a new field where you can put standard_price + additional costs (labels, shipping...)""")


    final_margin = fields.Float(
        compute="_compute_final_margin",
        string="Final margin",
        digits="Product Price",
        help="Final margin is [ sale price (Wo Tax) - Final cost ] "
        "of the product form (not based on historical values). "
        "Take care of tax include and exclude. If no sale price, "
        "the margin will be negativ.",
    )

    final_margin_rate = fields.Float(
        compute="_compute_final_margin",
        string="Final margin (%)",
        digits="Product Price",
        help="Margin rate is [ Final margin / sale price (Wo Tax) ] "
        "of the product form (not based on historical values)."
        "Take care of tax include and exclude.. If no sale price "
        "set, will display 999.0",
    )
    final_markup_rate = fields.Float(
        compute="_compute_final_margin",
        string="Final markup (%)",
        digits="Product Price",
        help="Markup rate is [ Final margin / cost price (Wo Tax) ] "
        "of the product form (not based on historical values)."
        "Take care of tax include and exclude.. If no cost price "
        "set, will display 999.0",
    )


    @api.depends_context('company')
    @api.depends('product_variant_ids', 'product_variant_ids.final_cost')
    def _compute_final_cost(self):
        # Depends on force_company context because final_cost is company_dependent
        # on the product_product
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.final_cost = template.product_variant_ids.final_cost
        for template in (self - unique_variants):
            template.final_cost = 0.0

    def _set_final_cost(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.final_cost = template.final_cost

    def _search_final_cost(self, operator, value):
        products = self.env['product.product'].search([('final_cost', operator, value)], limit=None)
        return [('id', 'in', products.mapped('product_tmpl_id').ids)]


    # Compute Section
    @api.depends(
        "list_price",
        "standard_price",
        "taxes_id.price_include",
        "taxes_id.amount",
        "taxes_id.include_base_amount",
    )
    def _compute_margin(self):
        # The code is duplicated from product.product model
        # because otherwise, the recomputation is not done correctly
        # when the product datas are changed from the template view
        for template in self:
            template.list_price_vat_excl = template.taxes_id.compute_all(
                template.list_price, product=template
            )["total_excluded"]
            template.standard_margin = (
                template.list_price_vat_excl - template.standard_price
            )
            if template.list_price_vat_excl == 0:
                template.standard_margin_rate = 999.0
            else:
                template.standard_margin_rate = (
                    (template.list_price_vat_excl - template.standard_price)
                    / template.list_price_vat_excl
                    * 100
                )
            if template.standard_price == 0:
                template.standard_markup_rate = 999.0
            else:
                template.standard_markup_rate = (
                    (template.list_price_vat_excl - template.standard_price)
                    / template.standard_price
                    * 100
                )

    @api.depends(
        "list_price",
        "taxes_id.price_include",
        "taxes_id.amount",
        "taxes_id.include_base_amount",
    )
    def _compute_final_margin(self):
        for template in self:
            template.list_price_vat_excl = template.taxes_id.compute_all(
                template.list_price, product=template
            )["total_excluded"]
            template.final_margin = (
                template.list_price_vat_excl - template.final_cost
            )
            if template.list_price_vat_excl == 0:
                template.final_margin_rate = 999.0
            else:
                template.final_margin_rate = (
                    (template.list_price_vat_excl - template.final_cost)
                    / template.list_price_vat_excl
                    * 100
                )
            if template.final_cost == 0:
                template.final_markup_rate = 999.0
            else:
                template.final_markup_rate = (
                    (template.list_price_vat_excl - template.final_cost)
                    / template.final_cost
                    * 100
                )

