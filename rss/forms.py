from django.forms import ModelForm
from .models import Url


class FormUrl(ModelForm):
    class Meta:
        model = Url
        fields = ['url', 'limit']