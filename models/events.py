# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Event(models.Model):

    _inherit = 'event.event'

    theme_event = fields.Char(string='Theme Event')
    organizer_ids = fields.One2many('organizer.mangament', 'event_id', string='organizer')
    material_list = fields.Many2many(comodel_name='event.material', string='material_event_rel')
    