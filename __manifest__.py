# -*- coding: utf-8 -*-
{
    'name': "Notify Sales",

    'summary': """
        Module Notify Sales""",

    'description': """
        Notify sales is a module that could send an notification to the client / users when we post an sales order
    """,

    'author': "Muhammad Ilmi Fauzan",
    'website': "www.linkedin.com/in/m-ilmi-fauzan",

    'category': 'Uncategorized',
    'version': '0.1',

		# Depencicy
    'depends': ['sale_management'],

		# Include ALL XML Code in Here be mindful of order
    'data': [
        'security/ir.model.access.csv',
        'views/config_notify.views.xml',
        'views/sales_inherit.views.xml',
        'views/res_partner_inherit.views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}