from odoo import models, fields, api


class ContractReport(models.AbstractModel):
    _name = 'report.school.report_classes_pdf'
    _description = 'Classes Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("tests--------------------------------------------")
        domain = [data['class_name']]
        students = self.env['school.student'].search(domain)
        tests = self.env['school.student'].search_read(domain)
        print(tests)
        print("tests--------------------------------------------")
        return {
            'students': students,
            'data': data,
        }
