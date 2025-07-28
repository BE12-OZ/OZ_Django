from django.test import TestCase
from django.urls import reverse

class AccountsViewTest(TestCase):
    def test_test_view(self):
        """accounts 앱의 test_view가 정상적으로 호출되는지 테스트"""
        response = self.client.get(reverse('test_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test view for accounts app")