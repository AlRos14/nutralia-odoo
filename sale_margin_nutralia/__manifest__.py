# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Final margins in Sales Orders - Nutralia Foods Version',
    'version':'1.0',
    'category': 'Sales/Sales',
    'description': """
This module adds the 'Final margin' on sales order.
=============================================

This gives the profitability by calculating the difference between the Unit
Price and Final Cost Price.
    """,
    'depends':['sale_management'],
    'data':[
        'views/sale_order_views.xml',
    ],
    'license': 'LGPL-3',
}
