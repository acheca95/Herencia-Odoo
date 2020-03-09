
from odoo import models, fields
from datetime import datetime

class Datos(models.Model):
    _name = 'cine.cartelera'

   

    Titulo = fields.Char('Titulo', required=True)
    Descripcion = fields.Text('Descripccion')
    Disponible = fields.Boolean('Disponible')
    Precio = fields.Float(digits=lambda cr: (32, 2))
    estreno = fields.Date('Fecha Estreno', required=True)
    portada = fields.Binary("Portada",Help="Seleccionar Portada")





