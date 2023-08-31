# -*- coding: utf-8 -*-
{
    'name': 'DEMO Odoo Bug',
    'version': '1.0.0',
    'category': 'Hidden',
    'summary': 'This module was made to demonstrate a bug in Odoo.',
    'depends': [
        'project'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
