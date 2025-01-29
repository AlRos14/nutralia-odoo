===================
Sale Margin Module
===================

This is a modified version of the **Sale Margin** module from **Odoo**, developed for Nutralia Foods, to enhance the margin calculation functionalities. The original module is licensed under LGPLv3, and this version includes additional options tailored to specific business needs.

Key Features
============

This module allows users to track and calculate margins for sale orders with enhanced functionalities, adding more precision and flexibility in margin calculations. The following modifications have been implemented:

1. **Final Margin Calculation**:
   - Introduces a new field: `final_margin`.
   - This field calculates the margin using a refined formula that considers additional business rules.

2. **Invoice-Based Margin Calculation**:
   - Adds an option to calculate the margin using only the **invoiced subtotal** (taxable amount) instead of the subtotal from sale orders.
   - This provides a more accurate view of margins by focusing exclusively on what has been invoiced rather than what was originally ordered.

Calculation Methods
===================

The margin calculations now offer two options:

1. **Order-Based Margin**:
   - Uses the sale order's taxable amount (subtotal) for margin computation.

2. **Invoice-Based Margin**:
   - Calculates the margin using the invoiced taxable amount (subtotal), allowing for greater accuracy based on completed invoices.

Both methods can be toggled based on your company's preference, ensuring flexibility in adapting to different accounting or business requirements.

Technical Details
=================

The modifications build on the original `sale_margin` module by introducing:
- A `final_margin` field in sale orders and invoices.
- A configuration option to toggle between **order-based** and **invoice-based** margin calculations.

Integration
===========

This module is fully integrated with Odoo's sales and invoicing workflows. It ensures that margin calculations adapt dynamically to the selected configuration, providing a seamless experience for users.

Configuration
=============

To configure the margin calculation method:
1. Navigate to **Settings > Sales > Margin Calculation**.
2. Select the desired method:
   - **Order-Based Margin**: Calculate margins using the sale order subtotal.
   - **Invoice-Based Margin**: Calculate margins using the invoiced subtotal.

Known Issues / Roadmap
======================

- **Multicurrency Support**: Currently, the margin calculation assumes that the sale order and invoice are in the same currency. Multicurrency support may be added in future versions.


Credits
=======

Authors
-------
- Odoo S.A. (Original author of the `sale_margin` module)

Contributors
------------
- Alejandro Rosado (Enhancements to margin calculations for Nutralia Foods)

License
=======

This module is licensed under the GNU LGPLv3, consistent with the original `sale_margin` module. For more details, refer to the [LICENSE](https://github.com/odoo/odoo/blob/16.0/LICENSE) file.

