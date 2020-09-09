# Copyright 2020 - TODAY, Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Repair lot_id required only ready state',
    'summary': """
        This module change traceability field required by state.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Escodoo,Odoo Community Association (OCA)',
    'website': 'https://github.com/oca/manufacture',
    'depends': [
        'repair',
        # 'web_action_conditionable',
    ],
    'data': [
        'views/repair_line.xml',
    ],

}
