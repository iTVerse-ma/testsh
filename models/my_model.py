from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Custom Model'

    name = fields.Char(string="Nom")
    description = fields.Text(string="Description")
    date_creation = fields.Datetime(string="Date de création", default=fields.Datetime.now)
    actif = fields.Boolean(string="Actif", default=True)
