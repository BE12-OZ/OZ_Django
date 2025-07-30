from django.urls import path
from . import views

app_name = 'bookmarks'
urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('create/', views.BookmarkCreateView.as_view(), name='bookmark_create'),
    path('<int:pk>/', views.bookmark_detail, name='bookmark_detail'),
]
