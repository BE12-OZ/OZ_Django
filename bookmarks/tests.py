from django.test import TestCase
from .models import Bookmark

class BookmarkModelTest(TestCase):
    def test_bookmark_creation(self):
        """Bookmark 모델이 정상적으로 생성되는지 테스트"""
        bookmark = Bookmark.objects.create(
            name="Test Bookmark",
            url="http://test.com"
        )
        self.assertEqual(bookmark.name, "Test Bookmark")
        self.assertEqual(bookmark.url, "http://test.com")
        self.assertEqual(str(bookmark), "Test Bookmark")
