# Lot Visibility

A module for Odoo that changes lot visibility.

### What It Does

This module creates a new view that inherits from stock.view_stock_move_line_detailed_operation_tree. If a lot's quantity is 0, the module will hide that lot in  **outgoing stock movements**. This helps inventory managers avoid mistakes when handling products with multiple lots.

### Bugs

This module has a known bug due to the way it operates. Lot visibility works by dynamically changing the domain in stock.move.line. However, for lines that already exist, the domain does not update dynamically because the triggers are not activated.

As a result, if you attempt to change the lot of an existing line, all lots will be displayed. To see only the available lots in stock, you must first select any lot. Once selected, reopen the lot selection, and you will see that the list is now correctly filtered.

#### Authors
- Alejandro Rosado

### License

This module is licensed under the GNU LGPLv3, respecting the original Odoo license.  
This is a gift to Nutralia Foods, shared with the community out of goodwill.
