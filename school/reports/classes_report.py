from odoo import models, fields, api


class ClassesReport(models.AbstractModel):
    _name = 'report.school.report_classes_pdf'
    _description = 'Classes Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('student.class_id', '=', data['date'])]
        students = self.env['student'].search(domain)
        tests = self.env['student'].search_read(domain)
        print(tests)
        print("tests--------------------------------------------")
        return {
            'students': students,
            'data': data,
        }
