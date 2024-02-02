# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

LOGGER = logging.getLogger(__name__)


class send_student_inherit(models.Model):
    _inherit = 'school.student'
    @api.model
    def create(self, vals):
        record = super(send_student_inherit, self).create(vals)

        fun_call = 'school.student/create_student'
        # send student data to other systems
        self.env['send_to'].send_to_system({'student_name': record.student_name, 'student_no': record.student_no,'birth_of_date': (record.birth_of_date).strftime("%Y-%m-%d"),'teacher_id': record.teacher_id.name,'gender': record.gender,'class_id': record.class_id.name_of_class,'subject_ids':[x.subject_name for x in record.subject_ids]}, fun_call)

        return record

    def write(self, vals):
        record = super(send_student_inherit, self).write(vals)

        fun_call = 'school.student/write_student'
        # send updated data to other systems
        self.env['send_to'].send_to_system({'student_name': self.student_name, 'student_no': self.student_no,'birth_of_date': (self.birth_of_date).strftime("%Y-%m-%d"),'teacher_id': self.teacher_id.name,'gender': self.gender,'class_id': self.class_id.name_of_class,'subject_ids':[x.subject_name for x in self.subject_ids]}, fun_call)

        return record

    def unlink(self):
        student_number = self.student_no

        record = super(send_student_inherit, self).unlink()

        fun_call = 'school.student/delete_student'

        self.env['send_to'].send_to_system({'student_no': student_number}, fun_call)
        return record
