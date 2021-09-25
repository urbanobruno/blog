from django.contrib import admin
from .models import Comentarios

# Register your models here.


class ComentariosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'email',
        'post',
        'data',
        'publicado',
    )
    list_display_links = ('id', 'nome', 'email')
    list_editable = ('publicado', )


admin.site.register(Comentarios, ComentariosAdmin)
