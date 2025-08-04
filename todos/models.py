from django.db import models
from django.conf import settings
from django_summernote.fields import SummernoteTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = SummernoteTextField(default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

