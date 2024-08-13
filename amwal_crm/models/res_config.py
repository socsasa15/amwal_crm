from odoo import models, fields


class InheritConfiguration(models.TransientModel):
    _inherit = "res.config.settings"

    unique_mobile = fields.Boolean(string="Unique Mobile Number", 
                    config_parameter="sttl_unique_contact_fields.unique_mobile")
    unique_email = fields.Boolean(string="Unique Email Id",
                    config_parameter="sttl_unique_contact_fields.unique_email")
