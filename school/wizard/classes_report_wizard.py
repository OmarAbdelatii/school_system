from odoo import models, fields, api


# wizard that take a class name and generate a report
class classWizard(models.TransientModel):
    _name = 'classes.wizard'
    _description = 'class Reports'

    class_name = fields.Char(string="Class Name", requird = True)

    def generate_report_class(self):
        print("000000######============",self.class_name)
        data = {
            "class_name": self.class_name,
        }
        print("000000######============", self.class_name)
        return self.env.ref('school.report_class_view').report_action(self, data = data)

