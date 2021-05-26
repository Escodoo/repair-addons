# Copyright 2020 - TODAY, Marcel Savegnago - Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class RepairLine(models.Model):

    _inherit = 'repair.line'

    order_state = fields.Selection(related='repair_id.state', store=True)

    @api.constrains('order_state','lot_id','product_id')
    def constrain_lot_id(self):
        x = 1
        # for line in self.filtered(
        #         lambda x: x.product_id.tracking != 'none' and not x.lot_id):
        #     if line.order_state == 'under_repair':
        #         raise ValidationError(_("Serial number is required for operation line"
        #                                 "with product '%s'") % line.product_id.name)