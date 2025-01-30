# Sale Margin - Modified Version for Nutralia Foods

This is a modified version of the **Sale Margin** module from **Odoo**, developed for Nutralia Foods, to enhance the margin calculation functionalities. 

### What It Does

This module uses the total cost, which is directly entered (product cost + additional costs such as labels, shipping, etc.) from the modified **product_standard_margin** module. It then calculates the final margin of the order based on this cost. If the quantity of products changes in the invoice, the margin is recalculated based on the invoiced amount.

### Credits

#### Authors
- Odoo S.A. (Original author of the `sale_margin` module)

#### Contributors
- Alejandro Rosado (Enhancements to margin calculations for Nutralia Foods)

### License

This module is licensed under the GNU LGPLv3, consistent with the original `sale_margin` module. For more details, refer to the [LICENSE](https://github.com/odoo/odoo/blob/16.0/LICENSE) file.
