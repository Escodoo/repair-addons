# Copyright 2020 - TODAY, Marcel Savegnago - Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class RepairOrder(models.Model):

    _inherit = 'repair.order'

    operations = fields.One2many(
        'repair.line', 'repair_id', 'Parts',
        copy=True, readonly=True,
        states = {
            'draft': [('readonly', False)],
            'confirmed': [('readonly', False)],
            'ready': [('readonly', False)],
        }
    )

    # state = fields.Selection([
    #     ('draft', 'Quotation'),
    #     ('cancel', 'Cancelled'),
    #     ('confirmed', 'Confirmed'),
    #     ('under_repair', 'Under Repair'),
    #     ('ready', 'Ready to Repair'),
    #     ('2binvoiced', 'To be Invoiced'),
    #     ('invoice_except', 'Invoice Exception'),
    #     ('done', 'Repaired')], string='Status',
    #     copy=False, default='draft', track_visibility='onchange',
    #     help="* The \'Draft\' status is used when a user is encoding a new and unconfirmed repair order.\n"
    #          "* The \'Confirmed\' status is used when a user confirms the repair order.\n"
    #          "* The \'Ready to Repair\' status is used to start to repairing, user can start repairing only after repair order is confirmed.\n"
    #          "* The \'To be Invoiced\' status is used to generate the invoice before or after repairing done.\n"
    #          "* The \'Done\' status is set when repairing is completed.\n"
    #          "* The \'Cancelled\' status is used when user cancel repair order.")