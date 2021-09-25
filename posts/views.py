from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Posts

# Todo
# Vantagem -> Pode reutilizar o codigo usando herança e etc


class PostIndex(ListView):
    model = Posts
    # ordering = '-id'
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'  # objeto mandado para o template


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass
