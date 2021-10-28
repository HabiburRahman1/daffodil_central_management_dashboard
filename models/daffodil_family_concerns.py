# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DaffodilFamilyConcerns(models.Model):
    _name = 'daffodil.family.concerns'
    _description = 'Daffodil Family Concerns'

    name = fields.Char(string="Institute Name")
    domain = fields.Char(string="Institute Domain")
    logo = fields.Char(string="Institute Logo")
    api_token = fields.Char(string="API Token")
    api_key = fields.Char(string="API Key")
    extension = fields.Char(string="Institute Extension")
    database_name = fields.Char(string="Database Name")
    admin_user_email = fields.Char(string="Admin Email")
    admin_user_password = fields.Char(string="Admin Password")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
