from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Имя')
    email = forms.CharField(required=True, label='Почта', widget=widgets.EmailInput())
    text = forms.CharField(max_length=3000, required=True, label='Текст',
                           widget=widgets.Textarea(attrs={'cols': 20, 'rows': 5}))
