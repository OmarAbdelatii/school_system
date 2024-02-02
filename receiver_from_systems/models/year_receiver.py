from odoo import models, fields, api


class year_inherit(models.Model):
    _inherit = 'school.year'

    def create_year(self, args=[], **kwargs):
        self = self.sudo()

        # parameters validations
     #   if not kwargs['no_classes'] or not isinstance(kwargs['no_classes'], int):
      #      return "not supported type we need it in numbers"
     #   if not kwargs['year'] or not isinstance(kwargs['year'], int):
     #       return "not supported type for year we need it in numbers"

        # fill data
        vals = {}
        vals['year'] = kwargs['year']
        vals['no_classes'] = kwargs['no_classes']

        self.env['school.year'].create(vals)

        return True


    def write_year(self, args=[], **kwargs):
        self = self.sudo()
        # fill data
        vals = {}
       # kwargs['year'] = self.env["school.year"].search([('year', '=', kwargs['year'])]).id
        vals['year'] = kwargs['year']

        vals['no_classes'] = kwargs['no_classes']
        print("------->", vals)
        self.env['school.year'].search([('year', '=', kwargs['year'])]).write(vals)

        return True

    def delete_year(self, args=[], **kwargs):
        self = self.sudo()

        self.env['school.year'].search([('year', '=', kwargs['year'])]).unlink()

        return True
