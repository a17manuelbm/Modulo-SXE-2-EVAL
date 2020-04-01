# -*- coding: utf-8 -*-
import logging
from datetime import datetime, date

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

class VideclubDirectores(models.Model):
    _name='videoclub.directores'
    _description='Videoclub Directores'
    _inherits={'res.partner': 'partner_id'}

    partner_id=fields.Many2one('res.partner',ondelete='cascade')
    nombre=fields.Char('Nombre',required=True)
    fecha_nacimiento=fields.Date('Fecha de nacimiento')
    foto=fields.Binary("Foto",related='partner_id.image')
    edad=fields.Integer('Edad', compute='calcular_edad')
    retirado=fields.Char('Retirado', default='No')
    state=fields.Selection([
        ('retirado','Retirado'),
        ('activo','En activo'),
        ('fallecido','Fallecido')],
        'State',default='activo')

    @api.multi
    def calcular_edad(self):
        fecha_nac = self.fecha_nacimiento
        fecha_actual = date.today()
        fecha_cunple = self.fecha_nacimiento.replace(year=fecha_actual.year)
        if fecha_cunple > fecha_actual:
            self.edad = fecha_actual.year - fecha_nac.year - 1
        else:
            self.edad = fecha_actual.year - fecha_nac.year
        return
    @api.constrains('fecha_nacimiento')
    def _comprobar_fecha_nacimiento(self):
        for r in self:
            if r.fecha_nacimiento >= fields.Date.today():
                raise models.ValidationError('Fecha de nacimiento erronea')

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('activo', 'retirado'),
                   ('activo', 'fallecido'),
                   ('retirado','fallecido'),
                   ('retirado','activo')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for director in self:
            if director.is_allowed_transition(director.state, new_state):
                director.state = new_state
            else:
                message = _('Moving from %s to %s is not allowed') % (director.state, new_state)
                raise UserError(message)

    def retirarse(self):
        self.change_state('retirado')

    def fallecer(self):
        self.change_state('fallecido')

    def volver(self):
        self.change_state('activo')

class VideoclubPelicula(models.Model):
    _name = 'videoclub.pelicula'
    _description = 'Peliculas'

    titulo= fields.Char('Titulo', required=True)
    genero = fields.Char('Generos')
    horas = fields.Integer('Duracion')
    directores=fields.Many2one('res.partner','Directores')

    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('nodisponible', 'Sin Stock')],
        'State', default="disponible")


class VideoclubAlquiler(models.Model):
    _name='videoclub.alquiler'
    _description='Videoclub Alquiler'

    nombre_peliculas=fields.Many2one('videoclub.pelicula',required=True)
    fecha_alquiler=fields.Date('Fecha de alquiler',default=lambda*a:datetime.now().strftime('%Y-%m-%d'))
    fecha_devolucion=fields.Date('Fecha devolucion',required=True)

    @api.constrains('fecha_alquiler','fecha_devolucion')
    def _comprobar_fechas_alquiler(self):
        for record in self:
            if record.fecha_alquiler > record.fecha_devolucion:
                raise models.ValidationError('Fecha devolucion no puede ser anterior a la de alquiler')
            elif record.fecha_alquiler < fields.Date.today():
                raise models.ValidationError('Fecha vencida')
            elif record.fecha_devolucion <= fields.Date.today():
                raise models.ValidationError('Fecha de devolucion no puede ser inferior o igual a la de alquier. Mínimo 1 día de alquiler')