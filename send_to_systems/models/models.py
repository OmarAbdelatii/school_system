# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class send_to_systems(models.Model):
#     _name = 'send_to_systems.send_to_systems'
#     _description = 'send_to_systems.send_to_systems'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
