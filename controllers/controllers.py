# -*- coding: utf-8 -*-
# from odoo import http


# class EventMangement(http.Controller):
#     @http.route('/event_mangement/event_mangement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_mangement/event_mangement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_mangement.listing', {
#             'root': '/event_mangement/event_mangement',
#             'objects': http.request.env['event_mangement.event_mangement'].search([]),
#         })

#     @http.route('/event_mangement/event_mangement/objects/<model("event_mangement.event_mangement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_mangement.object', {
#             'object': obj
#         })
