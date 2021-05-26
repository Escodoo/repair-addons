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