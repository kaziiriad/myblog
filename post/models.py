from django.db import models
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now, editable=False)
    body = models.TextField()
