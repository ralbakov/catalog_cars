from django import forms
from idea.models import CarMark, CarModel


class CarMarkForm(forms.Form):
    name = forms.ModelChoiceField(queryset=CarMark.objects.all(), label='Выберите марку')