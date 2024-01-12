from odoo import models, fields, api

class classWizard(models.TransientModel):
    _name ='classeswizard'
    _description ='class Reports'

    class_name = fields.Many2one('school.classes' , required = 'True')

    @api.model
    def _print_classes_report(self):
        data = {

            'class_name' : self.class_name,

        }
        return self.env.ref('school.report_contract_view').report_action(self, data = data)
