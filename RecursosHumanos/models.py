# -*- encoding: utf-8 -*-
from django.db import models

class Departamento(models.Model):
	nombre_departamento=models.CharField(max_length=20)

	class Meta:
		permissions = (("can_view_department", "Can view departamento"),("can_view_reports", "Can view reportes"),)

	def __unicode__(self):
		return self.nombre_departamento

class Cargo(models.Model):
	nombre_cargo=models.CharField(max_length=20)
	descripcion_cargo=models.TextField()
	salario_base=models.IntegerField()
	departamento=models.ForeignKey(Departamento)
	desempenio=models.IntegerField(null=True, blank=True)

	class Meta:
		permissions = (("can_view_charge", "Can view cargo"),)

	def __unicode__(self):
		return self.nombre_cargo