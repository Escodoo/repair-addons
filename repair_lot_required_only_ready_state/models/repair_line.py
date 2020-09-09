# Copyright 2020 - TODAY, Marcel Savegnago - Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class RepairLine(models.Model):

    _inherit = 'repair.line'

    # repair_order_state = fields.Many2one(
    #     'repair_order', string='Repair Order State', required=True, index=True,
    #     default=lambda self: self.repair_id.state,
    #     help="Repair Order State")

    # state_order = fields.Selection(related='repair_id.state', store=True, string='Order State')
    order_state = fields.Selection(related='repair_id.state', store=True)


    # @api.onchange('state')
    # def _onchange_product_id(self):
    #     if self.price_unit > 0.0:
    #         xyz = True
    #     else:
    #         xyz = False

    # @api.multi
    # @api.onchange('order_state')
    # def _onchange_product_id(self):
    #     if self.price_unit > 0.0:
    #         xyz = True
    #     else:
    #         xyz = False

    # @api.onchange('state_order')
    # def state_order(self):
    #     if self.state == "delivery_success":
    #         self.handed = True

    @api.constrains('order_state','lot_id','product_id')
    def constrain_lot_id(self):
        for line in self.filtered(lambda x: x.product_id.tracking != 'none' and not x.lot_id):
            if (line.order_state == 'under_repair'):
                raise ValidationError(_("Serial number is required for operation line with product '%s'") % (line.product_id.name))