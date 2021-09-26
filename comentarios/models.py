from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts
from django.utils import timezone

# Create your models here.


class Comentarios(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.nome
