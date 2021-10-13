from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Comentarios
import requests
from decouple import config


class ComentarioForm(ModelForm):
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

        # todo trocar
        if not request_result.get('success'):
            self.add_error(
                'comentario',
                'Intruso. Robô reconhecido.'
            )

        print(request_result)

        # todo check clean
        # super().clean()
