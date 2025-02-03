# Created by Alejandro Rosado for Nutralia Foods, LGPLv3 license.
from odoo import models, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    @api.onchange('picking_id', 'product_id', 'lot_id')
    def _onchange_picking_id(self):
        print("onchange de picking_id ejecutado")
        if self.picking_id.picking_type_id.code == "outgoing":
            return {'domain': {'lot_id': [('product_id', '=', self.product_id.id), 
                                          ('company_id', '=', self.company_id.id), 
                                          ('product_qty', '>', 0)]}}
        return {'domain': {'lot_id': [('product_id', '=', self.product_id.id), 
                                      ('company_id', '=', self.company_id.id)]}}
