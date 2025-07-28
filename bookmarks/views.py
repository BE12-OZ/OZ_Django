from django.shortcuts import render, get_object_or_404
from .models import Bookmark

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarks/bookmark_list.html', context)

def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    context = {'bookmark': bookmark}
    return render(request, 'bookmarks/bookmark_detail.html', context)