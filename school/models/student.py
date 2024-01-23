from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Information'
    _rec_name ='student_no'
    student_name = fields.Char(string="Student Name ", required=True)
    #Student Number
    student_no = fields.Char(string=" Student Number", required=True)
    birth_of_date = fields.Date(string="Birth of date" ,required=True)
    #for teachers
    teacher_id = fields.Many2one("res.users",string="Teacher")
    # Age field comuted from Bithdate field
    age = fields.Integer("Age", compute="_compute_age")
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], default='male')

    year_id = fields.Many2one(related="class_id.year_id", string='Year',store = True)
    class_id = fields.Many2one("school.classes", string="Class Name", ondelete="set null")
# one to many with Subject
    subject_ids = fields.Many2many("school.subject", inverse_name='student_ids', string="Subject", required=True)

# To compute Age field
    @api.depends('birth_of_date')
    def _compute_age(self):
        for r in self:
            if r.birth_of_date:
                r.age = date.today().year - r.birth_of_date.year
            else:
                r.age = 0

# Python Constrain On birth_of_date Field to ensure that the student has a right age
    @api.constrains("birth_of_date")
    def _check_birthdate(self):
        for r in self:
            if (date.today().year - r.birth_of_date.year) < 7:
                raise ValidationError("too young to be a student!!")
# SQL Constrain On student_no Field to accept only Unique Student Number
    _sql_constraints = [('student_unique_no', 'UNIQUE(student_no)', "The Student number Must be Unique")]
