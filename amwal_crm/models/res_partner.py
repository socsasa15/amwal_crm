from odoo import models, api
from odoo.exceptions import ValidationError


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"


    @api.constrains('email', 'mobile')
    def check_mobile_and_email(self):
        param_value_email = self.env['ir.config_parameter'].get_param('sttl_unique_contact_fields.unique_email')
        param_value_mobile = self.env['ir.config_parameter'].get_param('sttl_unique_contact_fields.unique_mobile')
        
        if param_value_email and param_value_mobile:
            for rec in self:
                if rec.email and rec.mobile:
                    contact = self.env['res.partner'].search([('email', '=', rec.email), ('id', '!=', rec.id), ('mobile', '=', rec.mobile)], limit=1)
                    if contact:
                        raise ValidationError("The Mobile Number and Email address are already associated with an existing contact. Please provide a unique Mobile Number and Email address for this contact")
                        return
                    contact_email = self.env['res.partner'].search([('email', '=', rec.email), ('id', '!=', rec.id)], limit=1)
                    if contact_email:
                        raise ValidationError("The Email address is already associated with an existing contact. Please provide a unique Email address for this contact")
                        return
                    contact_mobile = self.env['res.partner'].search([('mobile', '=', rec.mobile), ('id', '!=', rec.id)], limit=1)
                    if contact_mobile:
                        raise ValidationError("The Mobile number is already associated with an existing contact. Please provide a unique Mobile number for this contact")
                if rec.email:
                    contact = self.env['res.partner'].search([('email', '=', rec.email), ('id', '!=', rec.id)])
                    if contact:
                        raise ValidationError("The Email address is already associated with an existing contact. Please provide a unique Email address for this contact")
                if rec.mobile:
                    contact = self.env['res.partner'].search([('mobile', '=', rec.mobile), ('id', '!=', rec.id)])
                    if contact:
                        raise ValidationError("The Mobile number is already associated with an existing contact. Please provide a unique Mobile number for this contact")         
        elif param_value_email:
            for rec in self:
                if rec.email:
                    contact = self.env['res.partner'].search([('email', '=', rec.email), ('id', '!=', rec.id)])
                    if contact:
                        raise ValidationError("The Email address is already associated with an existing contact. Please provide a unique Email address for this contact")
        elif param_value_mobile:
            for rec in self:
                if rec.mobile:
                    contact = self.env['res.partner'].search([('mobile', '=', rec.mobile), ('id', '!=', rec.id)])
                    if contact:
                        raise ValidationError("The Mobile number is already associated with an existing contact. Please provide a unique Mobile number for this contact")

