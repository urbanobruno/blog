from django.db.models.functions import Concat
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from comentarios.models import Comentarios
from comentarios.forms import ComentarioForm
from .models import Posts
from django.db.models import Q, Count, Case, When, Value
from django.contrib import messages
from django.db import connection
from django.views import View


# Todo
# Vantagem -> Pode reutilizar o codigo usando herança e etc


class PostIndex(ListView):
    model = Posts
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'  # object sended to the template

    # todo estudar mais sobre select_related
    def get_queryset(self):
        qs = super().get_queryset().filter(publicado_post=True).select_related('categoria').order_by('-id').annotate(
            numero_comentarios=Count(
                Case(When(comentarios__publicado_comentario=True, then=1))
            )
        )
        return qs


class PostBusca(PostIndex):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # todo check
        termo = self.request.GET.get('termo', None)

        if termo:
            context['title'] = termo + ' | Search'

        return context

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
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # todo check
        context['title'] = self.kwargs.get('categoria').title() + ' | Categoria'
        return context

    def get_queryset(self):
        categoria = self.kwargs.get('categoria', None)
        qs = super().get_queryset().filter(
            categoria__nome__iexact=categoria
        )
        return qs


# class PostDetalhes(UpdateView):
#     template_name = 'posts/post_detalhes.html'
#     model = Posts
#     form_class = ComentarioForm
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.get_object()
#         comentarios = post.comentarios_set.filter(
#             publicado_comentario=True
#         )
#         context['comentarios'] = comentarios
#         return context
#
#     def form_valid(self, form):
#         post_id = self.get_object().id
#
#         comentario = Comentarios(
#             **form.cleaned_data,
#             post_id=post_id
#         )
#
#         if self.request.user.is_authenticated:
#             comentario.usuario_id = self.request.user.id
#
#         comentario.save()
#         messages.success(self.request, 'Comentário criado com successo')
#         return redirect('post_detalhes', pk=post_id)

class PostDetalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        post = get_object_or_404(Posts, pk=self.kwargs.get('pk'), publicado_post=True)

        self.context = {
            'post': post,
            'comentarios': post.comentarios_set.filter(
                publicado_comentario=True,
            ),
            'form': ComentarioForm(request.POST or None),
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = self.context['form']
        print(self.context)
        if form.is_valid():
            comentario = form.save(commit=False)
            if request.user.is_authenticated:
                comentario.user.id = request.user.id

            comentario.post.id = self.context['post'].id
            comentario.save()
            messages.success(request, 'Seu comentário foi enviado com successo para revisão.')
            return redirect('post_detalhes', pk=self.kwargs.get('pk'))

        return render(request, self.template_name, context=self.context)
