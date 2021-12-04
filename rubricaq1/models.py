import random
from odoo import models, fields, api




class ideas(models.Model):
    _name = 'ideas'
    name = fields.Char(string="Nombre ideas", required=True)
    apellido = fields.Char(string="llido ideas", required=True)
