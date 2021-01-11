from django import forms


class InputNameForm(forms.Form):
    name = forms.CharField(label='name', max_length=25)
