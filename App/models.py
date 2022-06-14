from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre=models.CharField(max_length=20, verbose_name="Nombre del Proyecto")
    descrip=models.TextField(max_length=250, verbose_name="Descripción del Proyecto")
    duracion=models.PositiveIntegerField(verbose_name="Duración del Proyect")
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio")
    activo=models.BooleanField(default=False)
    imagen=models.ImageField(upload_to='proyecto/', null= True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        db_table='proyectos'

