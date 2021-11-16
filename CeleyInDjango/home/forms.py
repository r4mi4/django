from django import forms


class NumberForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
