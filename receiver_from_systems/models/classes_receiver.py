from odoo import models, fields, api

import json

class classes_inherit(models.Model):
    _inherit = 'school.classes'

    def create_classes(self, args=[], **kwargs):
        self = self.sudo()

        # parameters validations
        if not kwargs['name_of_class'] or not isinstance(kwargs['name_of_class'], str):
            return "not supported type name of class"
        if not kwargs['year_id'] or not isinstance(kwargs['year_id'], int):
            return "not supported type for year we need it in numbers"

        # fill data
        vals = {}
        vals['name_of_class'] = kwargs['name_of_class']
        kwargs['year_id'] = self.env["school.year"].search([('year', '=',kwargs['year_id'])]).id

        vals['year_id'] = kwargs['year_id']

        self.env['school.classes'].create(vals)

        return True

