from odoo import api, fields, models


class Organizers(models.Model):
    
    _name = 'organizer.mangament'

    first_name = fields.Char(string='first name : ',required=True)
    last_name = fields.Char(string='last name : ')
    phone = fields.Char(string='Phone number : ')
    mail = fields.Char(string='Email : ')
    gender = fields.Selection(string='Gender :', selection=[('m', 'Male'), ('f', 'Femal')])
    event_id = fields.Many2one('event.event', string='Responser name :')
    partner = fields.Char(string='Partner : ')
    type_organizer = fields.Selection([('organization', 'Organization'),('customer', 'Customer')],string="Organization Type : "    )
    comp_name = fields.Char(string='Company name : ')
    comp_address = fields.Char(string='Company address : ')
    
    

