from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Departamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Municipio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(
        to=Departamento,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Canton(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(
        to=Municipio,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

class Direccion(models.Model):
    departamento = models.ForeignKey(to=Departamento, on_delete=models.CASCADE)
    municipio = models.ForeignKey(to=Municipio, on_delete=models.CASCADE)
    canton = models.ForeignKey(to=Canton, null=True, blank=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

class Problema(models.Model):
    origen = models.ForeignKey(to=Direccion, help_text="La dirección de su origen.")
    destino = models.ForeignKey(to=Direccion, help_text="La dirección de su destino.")
    categoria = models.ForeignKey(
        to=Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    usuario = models.ForeignKey(
        to=Usuario,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
