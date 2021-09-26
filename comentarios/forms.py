from django.forms import ModelForm
from .models import Comentarios


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = [
            'nome',
            'email',
            'comentario',
        ]

    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome')
        email = data.get('email')
        comentario = data.get('comentario')
        print(data)
