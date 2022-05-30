from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen', null=True)
    description = models.TextField(verbose_name="Descripción" ,null=True)
    
    # En __str__ si manipula la informacion mostrada en el administrador.
    def __str__(self):
        fila = 'Título: '+ self.title +' - Descripción: '+ self.description
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()