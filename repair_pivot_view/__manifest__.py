# Copyright 2020 - TODAY, Escodoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Repair Pivot View',
    'summary': """
        This module adds a pivot view for the repair orders""",
    'version': '12.0.1.0.0',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    'author': 'Escodoo,Odoo Community Association (OCA)',
    'website': 'https://github.com/oca/manufacture',
    'depends': [
        'repair',
    ],
    'data': [
        'views/repair_order.xml',
    ],
}
