# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class receiver_from_systems(models.Model):
#     _name = 'receiver_from_systems.receiver_from_systems'
#     _description = 'receiver_from_systems.receiver_from_systems'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
