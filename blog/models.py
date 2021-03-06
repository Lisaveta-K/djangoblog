from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = ImageField(upload_to='media')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title