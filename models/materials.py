from odoo import api, fields, models


class Material(models.Model):
    
    _name = 'event.material'

    mat_name = fields.Char(string='name :')
    matang_ids = fields.Many2many(
        comodel_name='material.equipment', 
        string='Equipment'
        )
    