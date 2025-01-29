# Product Margin and Margin Rate with Additional Costs

This module has been adapted by **Nutralia Foods** to include new functionalities for calculating product margins and markups. It now allows managing additional costs associated with each product, such as labels, shipping, or other custom costs. Additionally, the margin and markup fields have been recalculated to include these additional costs.

## Description

The module adds the following fields to the product form:

1. **Standard Margin:**  
   `(Sale price without taxes - Total product cost) / Sale price without taxes`.

2. **Margin (%):**  
   `(Standard margin / Sale price) * 100`.

3. **Standard Markup:**  
   `(Sale price without taxes - Total product cost) / Total product cost`.

4. **Total Product Cost:**  
   Calculated as:  
   `Product cost + Additional costs (entered directly in Odoo)`.

5. **Final Margin:**  
   `(Sale price without taxes - Total product cost) / Sale price without taxes`.

6. **Final Margin (%):**  
   `(Final margin / Sale price) * 100`.

7. **Final Markup:**  
   `(Sale price without taxes - Total product cost) / Total product cost`.

With these changes, the system provides a more accurate view of product margins and profitability by considering all relevant costs.

### Visual Example

![Product Form](https://raw.githubusercontent.com/OCA/margin-analysis/16.0/product_standard_margin/static/description/product_form.png)  
*Product form with the newly added fields.*

---

## Important Notes

- **Currency:** Price calculations require cost and sale prices to be in the same currency (default configuration in Odoo). This module does not manage automatic currency conversions.
- **Compatibility:** While it works in multi-company environments, prices must be correctly configured per company to avoid errors.

---

## Table of Contents

- [Description](#description)  
- [Important Notes](#important-notes)  
- [Known Issues / Roadmap](#known-issues--roadmap)  
- [Bug Tracking](#bug-tracking)  
- [Credits](#credits)  
- [Maintainers](#maintainers)

---

## Known Issues / Roadmap

- **Multi-company:** Not fully optimized for contexts where product prices depend on the company.

---

## Bug Tracking

Bugs are tracked on [GitHub Issues](https://github.com/OCA/margin-analysis/issues). In case of issues, check if your problem has already been reported. If not, help us by reporting it with details at the following link:  
[Report an Issue](https://github.com/OCA/margin-analysis/issues/new?body=module:%20product_standard_margin%0Aversion:%2016.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**).

---

## Credits

### Original Authors

- Camptocamp  
- GRAP  

### Contributors

- Alexandre Fayolle <alexandre.fayolle@camptocamp.com>  
- Yannick Vaucher <yannick.vaucher@camptocamp.com>  
- Joël Grand-Guillaume <joel.grand-guillaume@camptocamp.com>  
- Sylvain Le Gal (https://twitter.com/legalsylvain)  
- Cyril Vinh-Tung <cyril@invitu.com>  

### Adaptations for Nutralia Foods

- Alejandro Rosado

---

## Maintainers

This module has been adapted and is maintained by **Nutralia Foods** to manage additional costs and calculate more accurate margins.

The original code is maintained by the [Odoo Community Association (OCA)](https://odoo-community.org), a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To learn how to contribute, visit: [Contribute to OCA](https://odoo-community.org/page/Contribute).

## License

This module is licensed under the **AGPL-3.0** (GNU Affero General Public License v3.0), as maintained by the [Odoo Community Association (OCA)](https://odoo-community.org/page/license).