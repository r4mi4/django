from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm


class TestRegisterView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.failUnless(response.context['form'], UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('accounts:user_register'), data={
            'username': 'ramin',
            'email': 'ramin@email.com',
            'password1': 'ramin',
            'password2': 'ramin'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('accounts:user_register'), data={
            'username': 'ramin',
            'email': 'invalid_email',
            'password1': 'ramin',
            'password2': 'ramin'
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='email', errors=[
                             'Enter a valid email address.'])


class TestLoginView(TestCase):
    pass
