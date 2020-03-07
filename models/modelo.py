
from odoo import models, fields
from datetime import datetime

class Datos(models.Model):
    _name = 'multi.cartelera'
    _inherit='cine.cartelera'
   

    Duracion = fields.Integer('Duracion')
    Temporadas = fields.Float('Temporadas')





