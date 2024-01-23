from odoo import models, fields, api

import json

class SchoolClasses(models.Model):
    _name = 'school.classes'
    _description = 'School Classes'
    _rec_name = 'name_of_class'
    name_of_class = fields.Char('Class Name', required='True')
    year_id = fields.Many2one("school.year", string="Year", ondelete="set null")
    # unique class name
    _sql_constraints = [('classname_unique_no', 'UNIQUE(name_of_class)', "The Class name Must be Unique")]

