from django.db import models

# Create your models here.
class InfoGeneral(models.Model):
	nombre=models.CharField(max_length=66, default="Juanito")
	apellido = models.CharField(max_length=50, default="")
	telefono = models.CharField(max_length=50)
	fecha = models.DateField()
	semestre = models.CharField(max_length=50)
	carrera = models.CharField(max_length=50)
	SEXO_OPTIONS = (
		('F', 'FEMENINO'),
		('M', 'MASCULINO'),
		)
	sexo = models.CharField(max_length=50, choices=SEXO_OPTIONS)
	direccion = models.CharField(max_length=100)
	estructura = models.CharField(max_length=50, default="")