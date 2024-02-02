# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

LOGGER = logging.getLogger(__name__)


class send_subject_inherit(models.Model):
    _inherit = 'school.subject'

    @api.model
    def create(self, vals):
        record = super(send_subject_inherit, self).create(vals)

        fun_call = 'school.subject/create_subject'


        # send subject data to other systems

        self.env['send_to'].send_to_system({'subject_name': record.subject_name, 'year_id': record.year_id.year, 'student_ids': [x.student_no for x in record.student_ids] },fun_call)

        return record
    def write(self, vals):
        record = super(send_subject_inherit, self).write(vals)

        fun_call = 'school.subject/write_subject'
        # send updated data to other systems
        self.env['send_to'].send_to_system({'subject_name': self.subject_name, 'year_id': self.year_id.year, 'student_ids': [x.student_no for x in self.student_ids] },fun_call)

        return record
    def unlink(self):
        subj_name = self.subject_name

        record = super(send_subject_inherit, self).unlink()

        fun_call = 'school.subject/delete_subject'
        self.env['send_to'].send_to_system({'subject_name': subj_name}, fun_call)
        return record
