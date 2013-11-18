# -*- encoding: utf-8 -*-
from django.db import models
from Users.models import *

def to_json(obj):
		response_dict={}
		for field in obj._meta.fields:
			response_dict.update({field.name: str(getattr(obj, field.name))})
		if isinstance(obj, Factura):
			response_dict.update({'valor':obj._get_valor()})
		return response_dict

def ValuesQuerySetToDict(vqs):
		return [to_json(item) for item in vqs]

class Producto(models.Model):
	nombre_producto=models.CharField(max_length=20)
	descripcion_producto=models.TextField()
	cantidad_minima=models.IntegerField()
	precio_minimo=models.IntegerField()
	precio_maximo=models.IntegerField()

	def __unicode__(self):
		return self.nombre_producto

class SubCuenta(models.Model):
	numero_subcuenta=models.IntegerField()
	descripcion_subcuenta=models.TextField()

	def __unicode__(self):
		return unicode(self.numero_subcuenta)

class Cuenta(models.Model):
	numero_cuenta=models.IntegerField()
	descripcion_cuenta=models.TextField()
	subcuenta=models.ForeignKey(SubCuenta)

	def __unicode__(self):
		return '%s%s' % (self.numero_cuenta, self.subcuenta)

class Factura(models.Model):
	TIPO_FACTURA=(
		('C', 'Compra'),
		('V', 'Venta'),
	)

	cliente=models.ForeignKey(Persona, related_name='factura_clientes')
	fecha_factura=models.DateField()
	tipo_factura=models.CharField(max_length=15, choices=TIPO_FACTURA)
	empleado=models.ForeignKey(Persona, related_name='factura_empleados')
	cuenta=models.ForeignKey(Cuenta)

	#Factura de venta
	numero_factura=models.IntegerField(null=True, blank=True)

	def _get_valor(self):
		pedidos=Pedido_Venta.objects.filter(factura=self.id)
		sum=0
		for i in pedidos:
			sum=sum+(i.precio_unitario_venta*i.cantidad_venta)
		return sum

	def __unicode__(self):
		return unicode(self.id)

class Producto_Factura(models.Model):
	cantidad_venta=models.IntegerField()
	producto=models.ForeignKey(Producto)
	factura=models.ForeignKey(Factura)

	def __unicode__(self):
		return unicode(self.id)

class Liquidacion(models.Model):
	empleado=models.ForeignKey(Persona)
	fecha_liquidacion=models.DateField()
	valor=models.IntegerField()

	def _get_pago(self):
		return empleado.cargo.salario_base*(empleado.cargo.desempenio/100)
	
	def __unicode__(self):
		return '%s %s' % (self.empleado.get_full_name(), self.fecha_liquidacion)