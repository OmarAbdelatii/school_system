from odoo import models, fields, api

class ContractReportWizard(models.TransientModel):
    _name ='contract.wizard'
    _description =" Wizard"

    date = fields.Date(string="Date", requird = True)

    def generate_report_pdf(self):
        data = {
            "date": self.date,
        }
        return self.env.ref('school.report_contract_view').report_action(self, data = data)
