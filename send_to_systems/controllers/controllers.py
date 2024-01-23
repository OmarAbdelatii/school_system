# -*- coding: utf-8 -*-
# from odoo import http


# class SendToSystems(http.Controller):
#     @http.route('/send_to_systems/send_to_systems', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/send_to_systems/send_to_systems/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('send_to_systems.listing', {
#             'root': '/send_to_systems/send_to_systems',
#             'objects': http.request.env['send_to_systems.send_to_systems'].search([]),
#         })

#     @http.route('/send_to_systems/send_to_systems/objects/<model("send_to_systems.send_to_systems"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('send_to_systems.object', {
#             'object': obj
#         })
