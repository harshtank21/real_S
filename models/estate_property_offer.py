from odoo import models,fields


class Estat(models.Model):
    _name="estate.property.kk"
    _description="Property_dealer"

    price=fields.Float("Price")
    status=fields.Selection(([("accepted","ACCEPTED"),("refused","REFUSED")]),required="no copy")
    partner_id=fields.Many2one("res.partner",string="partner_id")
    # property_id=fields.Many2one("estate.property.kk",string="property_id")


