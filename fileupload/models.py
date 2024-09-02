from django.db import models

# Create your models here.
class Files(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    file = models.FileField(max_length=200, upload_to='uploads/')
    fecha = models.DateTimeField(auto_now=True)