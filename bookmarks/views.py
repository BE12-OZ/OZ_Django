from django.shortcuts import render
from .models import Bookmark

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarks/bookmark_list.html', context)