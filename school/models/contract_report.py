from odoo import models, fields, api


class ContractReport(models.AbstractModel):
    _name = 'report.school.report_contract_pdf'
    _description = 'Contract Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        domain = [('date_start', '<=', data['date']), ('state', '=', 'open')]
        employees = self.env['hr.contract.history'].search(domain)
        #tests = self.env['hr.contract.history'].search_read(domain)
        #print(tests)
        #print("tests--------------------------------------------")
        return {
            'employees': employees,
            'data': data,
        }
