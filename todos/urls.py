from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]