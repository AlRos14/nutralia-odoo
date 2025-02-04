# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modified by Alejandro Rosado for Nutralia Foods.
# This module is licensed under AGPLv3. It is a modification of the original
# sale_margin module, which was licensed under LGPLv3. 
# Ensure compliance with AGPLv3 terms when using this module.

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    final_margin = fields.Monetary("final_Margin", compute='_compute_final_margin', store=True)
    final_margin_percent = fields.Float("final_Margin (%)", compute='_compute_final_margin', store=True, group_operator="avg")

    @api.depends('order_line.final_margin', 'amount_untaxed')
    def _compute_final_margin(self):
        if not all(self._ids):
            for order in self:
                order.final_margin = sum(order.order_line.mapped('final_margin'))
                order.final_margin_percent = order.amount_untaxed and order.final_margin/order.amount_untaxed
        else:
            # On batch records recomputation (e.g. at install), compute the final_margins
            # with a single read_group query for better performance.
            # This isn't done in an onchange environment because (part of) the data
            # may not be stored in database (new records or unsaved modifications).
            grouped_order_lines_data = self.env['sale.order.line'].read_group(
                [
                    ('order_id', 'in', self.ids),
                ], ['final_margin', 'order_id'], ['order_id'])
            mapped_data = {m['order_id'][0]: m['final_margin'] for m in grouped_order_lines_data}
            for order in self:
                order.final_margin = mapped_data.get(order.id, 0.0)
                order.final_margin_percent = order.amount_untaxed and order.final_margin/order.amount_untaxed
