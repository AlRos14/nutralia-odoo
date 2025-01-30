# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Modified by Alejandro Rosado for Nutralia Foods, respecting the original LGPLv3 license.


{
    'name': 'Final margins in Sales Orders - Nutralia Foods Version',
    'version':'1.0',
    'category': 'Sales/Sales',
    'description': """
This module adds the 'Final margin' on sales order.
=============================================

This gives the profitability by calculating the difference between the Unit Price and Final Cost Price.
The margin will always be calculated using the base invoiced amount.

    """,
    'depends':['sale_management', 'product_standard_margin'],
    'data':[
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
}
