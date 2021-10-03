from django import template

register = template.Library()


# django variation of pluralize
@register.filter(name='pluraliza_comentarios')
def pluraliza_comentarios(obj):
    if isinstance(obj, (int, float)):
        if obj == 0:
            return f'Nenhum comentário'
        elif obj == 1:
            return f'{obj} comentário'
        else:
            return f'{obj} comentários'

    return
