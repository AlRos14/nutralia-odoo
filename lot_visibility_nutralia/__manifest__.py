# -*- coding: utf-8 -*-
# Created by Alejandro Rosado for Nutralia Foods, LGPLv3 license.


{
    'name': 'Lot visibility',
    'version':'1.0',
    'category': 'Stock/Stock',
    'description': """
This module uses the `product_qty` field from `stock.lot`. If a lot's quantity is 0, the module will hide that lot in **outgoing stock movements**. This helps inventory managers avoid mistakes when handling products with multiple lots.
=============================================
    """,
    'depends':['stock'],
    'license': 'LGPL-3',
}
