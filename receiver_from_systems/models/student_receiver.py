from odoo import models, fields, api
from datetime import date

class student_inherit(models.Model):
    _inherit = 'school.student'

    def create_student(self, args=[], **kwargs):
        self = self.sudo()

        # parameters validations
        if not kwargs['student_name'] or not isinstance(kwargs['student_name'], str):
            return "not supported type name "
        if not kwargs['student_no'] or not isinstance(kwargs['student_no'], str):
            return "not supported type IDbstudent"
        #if not kwargs['birth_of_date'] or not isinstance(kwargs['birth_of_date'], date):
        #    return "not supported type Date"
        #if not kwargs['teacher_id'] or not isinstance(kwargs['teacher_id'], str):
        #    return "not supported type for Teacher name"
        #if not kwargs['gender'] or not isinstance(kwargs['gender'], s):
        #    return "not supported type for Gender"
        #if not kwargs['class_id'] or not isinstance(kwargs['class_id'], str):
        #    return "not supported type for class"
        #if not kwargs['subject_ids'] or not isinstance(kwargs['subject_ids'], str):
        #   return "not supported type for Subject"

        # fill data
        vals = {}

        vals['student_name'] = kwargs['student_name']
        vals['student_no'] = kwargs['student_no']
       # kwargs['birth_of_date'] = self.env["school.student"].search([('birth_of_date', '=', kwargs['birth_of_date'])])

        vals['birth_of_date'] = kwargs['birth_of_date']

        kwargs['teacher_id'] = self.env["res.users"].search([('name', '=', kwargs['teacher_id'])]).id
        vals['teacher_id'] = kwargs['teacher_id']


        vals['gender'] = kwargs['gender']

        kwargs['class_id'] = self.env["school.classes"].search([('name_of_class', '=', kwargs['class_id'])]).id
        vals['class_id'] = kwargs['class_id']

        kwargs['subject_ids'] = [[6,0,self.env["school.subject"].search([('subject_name', 'in', kwargs['subject_ids'])]).ids]]





        vals['subject_ids'] = kwargs['subject_ids']

        self.env['school.student'].create(vals)

        return True