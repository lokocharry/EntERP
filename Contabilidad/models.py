# -*- encoding: utf-8 -*-
from __future__ import division
from django.db import models
from Users.models import *
from Logistica.models import Pagos_O_Descuentos
from datetime import date

def to_json(obj):
		response_dict={}
		for field in obj._meta.fields:
			response_dict.update({field.name: str(getattr(obj, field.name))})
		if isinstance(obj, Factura):
			response_dict.update({'valor':obj._get_valor()})
		return response_dict

def ValuesQuerySetToDict(vqs):
		return [to_json(item) for item in vqs]

class Cuenta(models.Model):
	numero_cuenta=models.IntegerField()
	descripcion_cuenta=models.TextField()

	class Meta:
		permissions = (("can_view_cuenta", "Can view cuenta"),)

	def __unicode__(self):
		return unicode(self.numero_cuenta)

class SubCuenta(models.Model):
	numero_subcuenta=models.IntegerField()
	descripcion_subcuenta=models.TextField()
	cuenta=models.ForeignKey(Cuenta)

	class Meta:
		permissions = (("can_view_subcuenta", "Can view subcuenta"),)

	def __unicode__(self):
		return u'%d%d' % (self.cuenta.numero_cuenta, self.numero_subcuenta)

class Producto(models.Model):
	nombre_producto=models.CharField(max_length=20)
	descripcion_producto=models.TextField()
	cantidad_minima=models.IntegerField()
	precio_minimo=models.IntegerField()
	precio_maximo=models.IntegerField()

	class Meta:
		permissions = (("can_view_producto", "Can view producto"),)

	def __unicode__(self):
		return self.nombre_producto

class Factura(models.Model):
	TIPO_FACTURA=(
		('C', 'Compra'),
		('V', 'Venta'),
	)

	cliente=models.ForeignKey(Persona, related_name='factura_clientes')
	fecha_factura=models.DateField()
	tipo_factura=models.CharField(max_length=15, choices=TIPO_FACTURA)
	empleado=models.ForeignKey(Persona, related_name='factura_empleados')
	productos=models.ManyToManyField(Producto, through='Producto_Factura')
	subcuenta=models.ForeignKey(SubCuenta)

	#Factura de venta
	numero_factura=models.IntegerField(null=True, blank=True)

	def _get_valor(self):
		pedidos=Producto_Factura.objects.filter(factura=self.id)
		total=0
		for i in pedidos:
			total=total+(i.producto.precio_minimo*i.cantidad)
		return total

	valor=property(_get_valor)
	
	class Meta:
		permissions = (("can_view_factura", "Can view factura"),("can_view_reports", "Can view reportes"),)

	def __unicode__(self):
		if self.numero_factura is not None:
			return u'%s (%s)' % (self.numero_factura, self.cliente)
		else:
			return unicode(self.id)

class Producto_Factura(models.Model):
	producto=models.ForeignKey(Producto)
	factura=models.ForeignKey(Factura)	
	cantidad=models.IntegerField()

class Liquidacion(models.Model):
	empleado=models.ForeignKey(Persona)
	fecha_liquidacion=models.DateField()
	valor=models.IntegerField(null=True, blank=True)

	def _get_pago(self):
		pago=self.empleado.cargo.salario_base*(self.empleado.cargo.desempenio/100)
		total=0
		pagosdescuentos=Pagos_O_Descuentos.objects.filter(empleado=self.empleado, fecha__year=date.today().year, fecha__month=date.today().month)
		for i in pagosdescuentos:
			total=total+i.valor
		return pago+total

	class Meta:
		permissions = (("can_view_liquidacion", "Can view liquidacion"),)
	
	def __unicode__(self):
		return '%s %s %s' % (self.empleado.nombre, self.empleado.apellido, self.fecha_liquidacion)