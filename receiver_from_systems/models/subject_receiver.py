from odoo import models, fields, api
from datetime import date

class subject_inherit(models.Model):
    _inherit = 'school.subject'

    def create_subject(self, args=[], **kwargs):
        self = self.sudo()

        # parameters validations
        if not kwargs['subject_name'] or not isinstance(kwargs['subject_name'], str):
            return "not supported type name "
        #if not kwargs['student_ids'] or not isinstance(kwargs['student_ids'], bool):
        #    return "not supported type IDS"
        if not kwargs['year_id'] or not isinstance(kwargs['year_id'], int):
            return "not supported type Date"

        # fill data
        vals = {}
        vals['subject_name'] = kwargs['subject_name']

########################################################
        #domain = [('student_no', '=', kwargs['student_ids'])]
        #kwargs['student_ids'] = self.env['school.student'].search(domain).id

      #  for rec in range(len(kwargs['student_ids'])):

      #      r[rec] = self.env["school.student"].search([('student_no', '=',rec)]).id
       #     print("______> ",r)
       #     vals['student_ids'] = rec
    ###########################################


        kwargs['student_ids'] =[[6,0, self.env["school.student"].search([('student_no', 'in',kwargs['student_ids'])]).ids]]


        vals['student_ids'] = kwargs['student_ids']




        kwargs['year_id'] = self.env["school.year"].search([('year', '=',kwargs['year_id'])]).id
        vals['year_id'] = kwargs['year_id']


        self.env['school.subject'].create(vals)

        return True