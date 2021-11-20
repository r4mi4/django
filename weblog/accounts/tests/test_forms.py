from django.test import SimpleTestCase, TestCase
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestRegistrationForm(TestCase):
    def test_valid_data(self):
        form = UserRegistrationForm(
            data={'username': 'ramimmn', 'email': 'ramin@email.com', 'password1': 'ramin', 'password2': 'ramin'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


class TestLoginForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserLoginForm(data={'username': 'ramin', 'password': 'ramin'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
