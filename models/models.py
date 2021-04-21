# Copyright 2020 Anvar Kildebekov <https://it-projects.info/team/fedoranvar>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import api, fields, models

class StockQuantBalance(models.Model):

    _inherit = 'stock.quant'

    @api.constrains('product_id')
    def check_product_id(self):
        pass

    def action_balance_qty(self):

        sqlscrpt=(
                "select product_id,location_id,location_dest_id,qty_done,lot_id "
                "from stock_move_line "
                "where state='done';"
                )

        for i in self.search([]):
            i.write({
                'quantity': 0
                })
        
        self._cr.execute(sqlscrpt)
        res = self._cr.dictfetchall()

        for i in res:
            sqrcrd = self.search([
                    ('product_id','=',i['product_id']),
                    ('location_id','=',i['location_id']),
                    ('lot_id','=', i.get('lot_id'))
                    ], limit=1)
            if len(sqrcrd) == 0:
                self.create({
                    'product_id': i['product_id'],
                    'location_id': i['location_id'],
                    'lot_id' : i.get('lot_id'),
                    'quantity': -i['qty_done']
                    })
            else:
                sqrcrd.write({
                    'quantity': sqrcrd.quantity - i['qty_done']
                    })

            sqrcrd = self.search([
                    ('product_id','=',i['product_id']),
                    ('location_id','=',i['location_dest_id']),
                    ('lot_id','=', i.get('lot_id'))
                    ], limit=1)
            if len(sqrcrd) == 0:
                self.create({
                    'product_id': i['product_id'],
                    'location_id': i['location_dest_id'],
                    'lot_id' : i.get('lot_id'),
                    'quantity': i['qty_done']
                    })
            else:
                sqrcrd.write({
                    'quantity': sqrcrd.quantity + i['qty_done']
                    })
