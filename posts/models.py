from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

# Create your models here.


class Posts(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo = models.TextField(verbose_name='Conteúdo')
    excerto = models.TextField(verbose_name='Excerto')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria'
    )
    imagem = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicar')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image(self.imagem, 800)

    @staticmethod
    def resize_image(image_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, image_name)
        img = Image.open(img_path)
        width, height = img.size
        if width <= new_width:
            img.close()
            return

        new_height = round((new_width * height) / width)
        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
        new_img.save(
            img_path,
            optimize=True,
            quality=60,
        )
        new_img.close()
