from django.urls import path
from . import views

urlpatterns = [
    path('', views.gugudan, name='gugudan'),
    path('<int:dan>/', views.gugudan_dan, name='gugudan_dan'),
]
