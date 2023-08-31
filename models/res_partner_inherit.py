# -*- coding: utf-8 -*-

from odoo import models, fields # Mandatory


class InheritResPartner(models.Model):
    _inherit = 'res.partner' #name of inherited existing odoo models

    id_telegram = fields.Char('ID Telegram') #adding field that store chat id telegram for notification