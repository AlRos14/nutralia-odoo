# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modified by Alejandro Rosado for Nutralia Foods.
# This module is licensed under AGPLv3. It is a modification of the original
# sale_margin module, which was licensed under LGPLv3. 
# Ensure compliance with AGPLv3 terms when using this module.


from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    final_margin = fields.Float(
        "Final margin", compute='_compute_final_margin',
        digits='Product Price', store=True, groups="base.group_user", precompute=True)
    final_margin_percent = fields.Float(
        "Final margin (%)", compute='_compute_final_margin', store=True, groups="base.group_user", precompute=True)
    total_cost = fields.Float(
        string="Total cost", compute="_compute_total_cost",
        digits='Product Price', store=True, readonly=False, copy=False, precompute=True,
        groups="base.group_user")

    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom')
    def _compute_total_cost(self):
        for line in self:
            if not line.product_id:
                line.total_cost = 0.0
                continue
            line = line.with_company(line.company_id)
            product_cost = line.product_id.final_cost
            line.total_cost = line._convert_price(product_cost, line.product_id.uom_id)

    @api.depends('qty_invoiced', 'price_subtotal', 'product_uom_qty', 'total_cost')
    def _compute_final_margin(self):
        for line in self:
            invoiced_qty = line.qty_invoiced
            if invoiced_qty > 0:
                price_subtotal = line.price_unit * invoiced_qty
                line.final_margin = price_subtotal - (line.total_cost * invoiced_qty)
                line.final_margin_percent = price_subtotal and line.final_margin / price_subtotal
            else:
                line.final_margin = line.price_subtotal - (line.total_cost * line.product_uom_qty)
                line.final_margin_percent = line.price_subtotal and line.final_margin / line.price_subtotal

    def _convert_price(self, product_cost, from_uom):
        self.ensure_one()
        if not product_cost:
            # If the standard_price is 0
            # Avoid unnecessary computations
            # and currency conversions
            if not self.total_cost:
                return product_cost
        from_currency = self.product_id.cost_currency_id
        to_cur = self.currency_id or self.order_id.currency_id
        to_uom = self.product_uom
        if to_uom and to_uom != from_uom:
            product_cost = from_uom._compute_price(
                product_cost,
                to_uom,
            )
        return from_currency._convert(
            from_amount=product_cost,
            to_currency=to_cur,
            company=self.company_id or self.env.company,
            date=self.order_id.date_order or fields.Date.today(),
            round=False,
        ) if to_cur and product_cost else product_cost
        # The pricelist may not have been set, therefore no conversion
        # is needed because we don't know the target currency..

    #if qty_invoiced change the order will be updated
    def write(self, vals):
        res = super().write(vals)
        if 'qty_invoiced' in vals:
            self.order_id._compute_final_margin()
        return res