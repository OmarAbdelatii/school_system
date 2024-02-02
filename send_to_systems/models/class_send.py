# -*- coding: utf-8 -*-

from odoo import models, fields, api


import logging

LOGGER = logging.getLogger(__name__)


class send_class_inherit(models.Model):
    _inherit = 'school.classes'



    @api.model
    def create(self, vals):
        record = super(send_class_inherit, self).create(vals)

        # send class data to other systems
        fun_call = 'school.classes/create_classes'
        self.env['send_to'].send_to_system({'name_of_class': record.name_of_class, 'year_id': record.year_id.year},fun_call)

        return record

    def write(self,vals):

        record = super(send_class_inherit, self).write(vals)

        fun_call = 'school.classes/write_classes'
        # send updated data to other systems
        self.env['send_to'].send_to_system({'name_of_class': self.name_of_class, 'year_id': self.year_id.year},fun_call)
        return record

    def unlink(self):
        class_n = self.name_of_class

        record = super(send_class_inherit, self).unlink()

        fun_call = 'school.classes/delete_class'
        self.env['send_to'].send_to_system({'name_of_class': class_n}, fun_call)
        return record
