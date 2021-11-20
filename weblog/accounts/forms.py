from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your password'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'enter your confirm password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError(
                'this email already exists ! plz enter enother one')
        return email

    # pass2 : because if use pass1 ,pass2  not created yet and we get an error
    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise forms.ValidationError('password must match')
    #     return p2

    # todo: this way recommend by django Documentation
    def clean(self):
        clean_data = super().clean()
        p1 = clean_data.get('password1')
        p2 = clean_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('password must match')
