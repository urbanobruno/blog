from django.contrib import admin
from .models import Posts
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostsAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'data',
                    'categoria', 'publicado_post',)
    list_display_links = ('id', 'titulo',)
    list_editable = ('publicado_post',)
    summernote_fields = ('conteudo', )


admin.site.register(Posts, PostsAdmin)
