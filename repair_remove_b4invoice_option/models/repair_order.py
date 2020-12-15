# Copyright 2020 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RepairOrder(models.Model):

    _inherit = 'repair.order'

    invoice_method = fields.Selection([
        ("none", "No Invoice"),
        ("after_repair", "After Repair")], string="Invoice Method",
        default='none', index=True, readonly=True, required=True,
        states={'draft': [('readonly', False)]},
        help='Selecting \'After Repair\' will allow you to generate invoice after the repair is done respectively. \'No invoice\' means you don\'t want to generate invoice for this repair order.')
