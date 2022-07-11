from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre=models.CharField(max_length=250, verbose_name="Nombre del Proyecto")
    descrip=models.TextField(max_length=250, verbose_name="Descripción del Proyecto")
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio")
    activo=models.BooleanField(default=False)
    imagen=models.ImageField(upload_to='proyecto/', null= True, blank=True)
    file=models.FileField(upload_to='proyecto/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        db_table='proyectos'

class FichaProyecto(models.Model):
    nombre_programa = models.CharField(max_length=250, verbose_name="Nombre del Programa")
    nombre_proyecto = models.TextField(max_length=250, verbose_name="Nombre del proyecto")
    codigo_proyecto = models.TextField(max_length=250, verbose_name="Código del proyecto")
    clasificación_proyecto = models.TextField(max_length=250, verbose_name="Clasificación del proyecto")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    activo = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='proyecto/', null=True, blank=True)
    file = models.FileField(upload_to='proyecto/', null=True, blank=True)