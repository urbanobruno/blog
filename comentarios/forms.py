from django import forms
from .models import Comentarios
import requests
from decouple import config


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = [
            'nome',
            'email',
            'comentario',
        ]

    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': config('SECRET_RECAPTCHA_KEY'),
                'response': recaptcha_response,
            }
        )
        request_result = recaptcha_request.json()

        if not request_result.get('success'):
            self.add_error(
                'comentario',
                'Favor preenche o campo "Não ou um robô" abaixo.'
            )


