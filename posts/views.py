from django.db.models.functions import Concat
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from comentarios.forms import ComentarioForm
from .models import Posts
from django.db.models import Q, Count, Case, When, Value


# Todo
# Vantagem -> Pode reutilizar o codigo usando herança e etc


class PostIndex(ListView):
    model = Posts
    ordering = '-id'
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'  # object sended to the template

    def get_queryset(self):
        qs = super().get_queryset().filter(publicado_post=True).annotate(
            numero_comentarios=Count(
                Case(When(comentarios__publicado_comentario=True, then=1))
            )
        )
        return qs


    # def get_queryset(self):
    #     qs = super().get_queryset()

# todo usar mesmo template do index
class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo', None)

        if not termo:
            return qs

        qs = qs.annotate(
            nome_autor=Concat('autor__first_name', Value(' '), 'autor__last_name')
        ).filter(
            Q(titulo__icontains=termo) |
            Q(autor__username__icontains=termo) |
            Q(nome_autor=termo) |
            Q(excerto__icontains=termo) |
            Q(categoria__nome__icontains=termo)
        )
        return qs


# todo usar mesmo template do index
class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        categoria = self.kwargs.get('categoria', None)
        qs = super().get_queryset().filter(
            categoria__nome__iexact=categoria
        )
        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Posts
    form_class = ComentarioForm
    context_object_name = 'post'
