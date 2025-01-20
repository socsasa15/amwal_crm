# -*- coding: utf-8 -*-

from odoo import models, api,_
from odoo.exceptions import ValidationError

class phone_unique(models.Model):
    _inherit='res.partner'

    @api.constrains('phone')
    def check_phone(self):
        for rec in self:
            if rec.phone != False:
                h = self.env['res.partner'].sudo().search(['|', ('phone','=', rec.phone), ('mobile','=', rec.phone), ('id','!=',rec.id)])
                if len(h) > 0:
                    raise ValidationError(_('Phone must be unique.'))


    @api.constrains('mobile')
    def check_mobile(self):
        for rec in self:
            if rec.mobile != False:
                k = self.env['res.partner'].sudo().search(['|', ('phone', '=', rec.mobile), ('mobile', '=', rec.mobile), ('id', '!=', rec.id)])
                if len(k) > 0:
                    raise ValidationError(_('Mobile must be unique.'))

class crm_phone_unique(models.Model):
    _inherit='crm.lead'

    _sql_constraints = [
        ('phone_unique', 'unique(phone)', 'Phone already exists!'),
        ('mobile_unique', 'unique(mobile)', 'Mobile already exists!')
    ]

    @api.constrains('phone')
    def check_phone_crm(self):
        for rec in self:
            if rec.phone != False:
                h = self.env['crm.lead'].sudo().search([('phone','=', rec.phone), ('id','!=',rec.id)])
                if len(h) > 0:
                    raise ValidationError(_('Phone must be unique..'))
                   
    @api.constrains('mobile')
    def check_mobile_crm(self):
        for rec in self:
            if rec.mobile != False:
                k = self.env['crm.lead'].sudo().search([('mobile', '=', rec.mobile), ('id', '!=', rec.id)])
                if len(k) > 0:
                    raise ValidationError(_('Mobile must be unique..'))