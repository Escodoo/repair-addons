# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, _
from odoo.exceptions import UserError


class RepairOrder(models.Model):

    _inherit = 'repair.order'

    def unlink(self):
        for order in self:
            if order.state not in ('draft', 'cancel'):
                raise UserError(
                    _('You can not delete a repair order once it has been confirmed. You must first cancel it.'))
            if order.state == 'cancel' and order.invoice_id and order.invoice_id.posted_before:
                raise UserError(
                    _('You can not delete a repair order which is linked to an invoice which has been posted once.'))
        return super().unlink()