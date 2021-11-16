from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:num_id>/', views.sum, name='sum')
]
