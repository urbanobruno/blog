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

        # todo see Validation Error
        # todo tirar
        if len(nome) < 5:
            self.add_error(
                'nome',
                'nome precisa ser maior que 5 caracteres.'
            )
