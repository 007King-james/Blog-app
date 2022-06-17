from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Title(models.Model):
    Title = models.CharField(max_length=200)
class author(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class text(models.Model):
    text = models.TextField
class created_date(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
class published_date(models.Model):
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

