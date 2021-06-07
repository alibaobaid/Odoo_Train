from odoo import api, fields, models


class equipment(models.Model):
    _name = 'material.equipment'

    name = fields.Char(string='Name')
