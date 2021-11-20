from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import user_register, user_login, user_logout


class TestUrls(SimpleTestCase):
    def test_register(self):
        url = reverse('accounts:user_register')
        self.assertEqual(resolve(url).func, user_register)

    def test_login(self):
        url = reverse('accounts:user_login')
        self.assertEqual(resolve(url).func, user_login)

    def test_logout(self):
        url = reverse('accounts:user_logout')
        self.assertEqual(resolve(url).func, user_logout)
