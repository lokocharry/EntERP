# -*- encoding: utf-8 -*-
from django.db import models

class Departamento(models.Model):
	nombre_departamento=models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre_departamento

class Cargo(models.Model):
	nombre_cargo=models.CharField(max_length=20)
	desceripcion_cargo=models.TextField()
	salario_base=models.IntegerField()
	departamento=models.ForeignKey(Departamento)
	desempenio=models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.nombre_cargo