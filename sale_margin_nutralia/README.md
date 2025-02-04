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

This module is licensed under the GNU AGPLv3. 

It is a modification of the original `sale_margin` module, which is licensed under GNU LGPLv3. The decision to license `sale_margin_nutralia` under AGPLv3 is due to its interaction with the `product_standard_margin` module, which is also licensed under AGPLv3. 

The AGPLv3 ensures that any derivative work remains free and open-source, providing users with the right to access, modify, and distribute the code. This change is necessary to maintain compatibility with the AGPLv3-licensed module and to uphold the principles of software freedom.

For more details, refer to the [LICENSE](https://github.com/odoo/odoo/blob/16.0/LICENSE) file.
