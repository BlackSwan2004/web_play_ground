from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):

    title = models.CharField(max_length=45, verbose_name='Titulo')
    #instalar ckeditor (pip install django-ckeditor)
    content = RichTextField(verbose_name='Contenido')
    orden = models.IntegerField(verbose_name='Orden', default=0)
    
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        db_table = 'Paginas'
        ordering = ['id']

    def __str__(self):
        return self.title