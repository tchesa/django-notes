from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
