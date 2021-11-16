from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('one/', views.one, name='one'),
    # path('person/', views.Persons, name='persons'),
    # path('person/<int:id>/', views.person, name='person'),
    # path('person-create/', views.person_create, name='person_create'),
]
