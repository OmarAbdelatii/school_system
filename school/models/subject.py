from odoo import models, fields, api


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subjects'
    _rec_name = 'subject_name'
    subject_name = fields.Char(string="Subject", required=True)

    student_ids= fields.Many2many("school.student",string="Student ID")

    year_id = fields.Many2one("school.year", string="Year", required=True)
    # SQL Constrain On student_no Field to accept only Unique Student Number
    _sql_constraints = [('subject_unique', 'Check(1=1)',"The Subject Must be Unique")]
