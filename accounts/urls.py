from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('', include('django.contrib.auth.urls')),
]
