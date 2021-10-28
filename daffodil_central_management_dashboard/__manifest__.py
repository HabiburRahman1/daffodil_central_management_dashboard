# -*- coding: utf-8 -*-
{
    'name': "Central Management Dashboard of Daffodil Family",

    'summary': """
        Central Management Dashboard of Daffodil Family""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Md Habibur Rahman",
    'website': "http://pd.daffodilvarsity.edu.bd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.14',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'project',
        'website',
        'event',
        'sale',
        'hr',
        'crm',
        'website_support',
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/central_management_dashboard_template.xml',
        'views/central_management_concerns_dashboard_template.xml',
        'views/central_management_module_support_ticket_dashboard_template.xml',
        'views/central_management_concerns_project_dashboard_template.xml',
        'views/central_management_module_project_task_dashboard_template.xml',
        'views/central_management_module_event_dashboard_template.xml',
        'views/central_management_module_employee_dashboard_template.xml',
        'views/central_management_module_opportunity_dashboard_template.xml',
        'views/central_management_module_accounts_dashboard_template.xml',
        'views/daffodil_family_ai_analytics_template.xml',
        'views/daffodil_family_concerns_view.xml',
        'security/security.xml',
        'views/menus.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
