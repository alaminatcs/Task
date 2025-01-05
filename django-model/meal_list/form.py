from django import forms

class djangoForm(forms.Form):
    name = forms.CharField(label = 'Enter your name: ')
    email = forms.EmailField(label = 'Put you mail address: ')
