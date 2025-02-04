# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modified by Alejandro Rosado for Nutralia Foods.
# This module is licensed under AGPLv3. It is a modification of the original
# sale_margin module, which was licensed under LGPLv3. 
# Ensure compliance with AGPLv3 terms when using this module.


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
