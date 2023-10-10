from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#HAY QUE INSTALAR TIME EN EL ENTORNO
import time
'''
PAra activar y actualizar los modelos hay que hacer
python manage.py makemigrations
python manage.py migrate

Los siguientes son los modelos creados en tablas, si queremos borrarlos bastara con
borrarlos de models.py
'''
class Datosusuario(models.Model):
    usuario              = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", default='defecto.png', blank=True, null=True)
    nombre               = models.CharField(max_length=50)
    apellido             = models.CharField(max_length=50)
    fecha_nacimiento     = models.DateField(blank=True, null=True)
    pais                 = models.CharField(max_length=30, blank=True)
    provincia            = models.CharField(max_length=40, blank=True)
    ciudad               = models.CharField(max_length=40, blank=True)
    domicilio            = models.CharField(max_length=80, blank=True)
    codigo_postal        = models.CharField(max_length=50, blank=True)
    telefono             = models.CharField(max_length=30, blank=True)
    celular              = models.CharField(max_length=30, blank=True)
    documento            = models.CharField(max_length=30, blank=True)
    cuit                 = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.usuario.username
