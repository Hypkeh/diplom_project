from django import forms
from django.forms import ModelForm
from .models import Announcment
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    q = forms.CharField(max_length=20, label='Поиск по словам')


class AnnouncmentForm(ModelForm):

    class Meta:
        model = Announcment
        fields = '__all__'
