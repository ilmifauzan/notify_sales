# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory


class ConfigNotify(models.Model):
    _name = 'notify_sales.config_notify' # format = name_of_module.name_of_class 
    _description = 'Config of Notify' # Some note of table
    _rec_name = 'telegram_api' # this is for naming of record, many case use 'name' field

    #usualy we insert field 'name' for search requirement, but in this case i didn't insert it beacuse it will be a waste field

    telegram_api = fields.Char('Telegram API') #adding field that store chat id telegram for notification
    template = fields.Text('Template') #text for adding template of notification
    active = fields.Boolean('Active') #in some condition should use another naming for active, because 'active' is odoo default field