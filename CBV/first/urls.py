from django.urls import path
from . import views

app_name = 'first'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.TodoCreat.as_view(), name='create'),
    path('Delete/<int:pk>', views.TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', views.UpdateTodo.as_view(), name='update'),
    path('<slug:myslug>/', views.DetailTodo.as_view(), name='Detail_Todo'),
    path('<int:year>/<str:month>', views.MonthTodo.as_view(), name='month_todo')

]
