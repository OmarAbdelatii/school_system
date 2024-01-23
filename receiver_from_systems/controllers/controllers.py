# -*- coding: utf-8 -*-
# from odoo import http


# class ReceiverFromSystems(http.Controller):
#     @http.route('/receiver_from_systems/receiver_from_systems', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/receiver_from_systems/receiver_from_systems/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('receiver_from_systems.listing', {
#             'root': '/receiver_from_systems/receiver_from_systems',
#             'objects': http.request.env['receiver_from_systems.receiver_from_systems'].search([]),
#         })

#     @http.route('/receiver_from_systems/receiver_from_systems/objects/<model("receiver_from_systems.receiver_from_systems"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('receiver_from_systems.object', {
#             'object': obj
#         })
