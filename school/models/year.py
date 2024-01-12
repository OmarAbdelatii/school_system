from odoo import models, fields, api


class SchoolYear(models.Model):
    _name = 'school.year'
    _description = 'School Year'
    _rec_name = 'year'
    year = fields.Integer('Year', required=True)
    no_classes = fields.Integer('Number of classes', required=True)
    # Year have to be unique
    _sql_constraints = [('year_unique_no', 'UNIQUE(year)', "Year have to be Unique")]
