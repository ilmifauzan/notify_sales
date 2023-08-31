# -*- coding: utf-8 -*-

from odoo import models, fields, api # Mandatory
import requests #this is request for api send telegram
from odoo.exceptions import ValidationError #this is for send pop up when error is call
import urllib #this is for parsing message url api telegram

class InheritSales(models.Model):
    _inherit = 'sale.order' #name of inherited existing odoo models

    send_notify = fields.Boolean('Send Notify?') #add boolean value, for option sending notify

    #adding function trigger on approve / confirming sale order
    @api.model
    def action_confirm(self,order): #this is function name of confirming sale order
        data_sale = self.env['sale.order'].search([('id', '=', order)]) #find sale order data
        if data_sale.send_notify == True:
            data_config = self.env['notify_sales.config_notify'].search([('active', '=', True)]) #find data config for finding api telegram and template message
            if data_config:
                if not data_config.telegram_api: #validation if telegram API is empty, minimalize unknown error
                    raise ValidationError('Telegram API is not found, please call your Sales Administrator!')
                if not data_sale.partner_id.id_telegram: #validation if partner telegram chat id is empty, minimalize unknown error
                    raise ValidationError('Telegram Chat ID partner is not found, please call your Sales Administrator!')
                message = data_config.template

                #this is for changing tags on template, make it more dynamic
                message = message.replace('<name>', str(data_sale.partner_id.name)) 
                message = message.replace('<no_sales>', str(data_sale.name))
                #

                message = urllib.parse.quote(message) 
                url = "https://api.telegram.org/bot" + str(data_config.telegram_api) + "/sendMessage?text=" + message + "&chat_id=" + str(data_sale.partner_id.id_telegram) # this is format url for call api telegram
                requests.get(url) #send request api