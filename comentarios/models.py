from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts
from django.utils import timezone

# Create your models here.


class Comentarios(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    comentario = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.nome
