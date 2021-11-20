from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


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
    def setUp(self):
        self.client = Client()
        User.objects.create_user('ramin','ramin@email.com','ramin')

    def test_user_login_GET(self):
        response = self.client.get(reverse('accounts:user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'accounts/login.html')
        self.failUnless(response.context['form'],UserLoginForm)

    def test_user_login_POST_valid(self):
        response = self.client.post(reverse('accounts:user_login'),data={
            'username': 'ramin',
            'password': 'ramin'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)

    def test_user_login_POST_invalid(self):
        response = self.client.post(reverse('accounts:user_login'),data={
            'username':'ramin',
            'password': 'ali'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)

class TestLogout(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user('ramin','ramin@email.com','ramin')
        self.client.login(username = 'ramin', password = 'ramin')

    def test_logout(self):
        response = self.client.get(reverse('accounts:user_logout'),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)


