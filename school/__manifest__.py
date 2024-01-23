# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """School Managment""",

    'description': """ School """,

    'author': "Omar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/year.xml',
        'views/classes.xml',
        'views/subject.xml',
        'views/student.xml',
        'reports/invoice_inherit_view.xml',
        'views/contractwizard.xml',
        'reports/contract_report.xml',
        'views/classeswizard.xml',
        'reports/classes_report_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
