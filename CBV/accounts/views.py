from django.shortcuts import render
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy


class UserLogin(auth_view.LoginView):
    template_name = 'accounts/login.html'


class UserPassReset(auth_view.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PasswordResetDone(auth_view.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'


class PasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_view.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
