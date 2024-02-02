# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

LOGGER = logging.getLogger(__name__)


class send_year_inherit(models.Model):
    _inherit = 'school.year'

    @api.model
    def create(self, vals):
        record = super(send_year_inherit, self).create(vals)
        fun_call = 'school.year/create_year'

        # send year data to other systems
        self.env['send_to'].send_to_system({'year': record.year, 'no_classes': record.no_classes},fun_call)

        return record

    def write(self,vals):

        record = super(send_year_inherit, self).write(vals)

        fun_call = 'school.year/write_year'
        # send updated data to other systems
        self.env['send_to'].send_to_system({'year': self.year, 'no_classes':  self.no_classes}, fun_call)
        return record

    def unlink(self):
        year = self.year
        record = super(send_year_inherit, self).unlink()

        fun_call = 'school.year/delete_year'
        self.env['send_to'].send_to_system({'year': year}, fun_call)
        return record

#["year.id","=",filter]