# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modified by Alejandro Rosado for Nutralia Foods, respecting the original LGPLv3 license.


from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    final_margin = fields.Float('Final margin')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['final_margin'] = f"""SUM(l.final_margin
            / {self._case_value_or_one('s.currency_rate')}
            * {self._case_value_or_one('currency_table.rate')})
        """
        return res
