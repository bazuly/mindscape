from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os


def upload_to(instance, filename):
    return os.path.join("news", instance.title, filename)


class NewsUpdateModel(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return self.title


class AboutModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = RichTextUploadingField()

    def __str__(self):
        return self.title


class FAQModel(models.Model):
    question = models.CharField(max_length=264)
    body = models.TextField()

    def __str__(self):
        return self.question
