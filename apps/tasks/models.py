from django.db import models
from django.contrib.auth.models import User

from apps.labels.models import Labels

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None, blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    labels = models.ManyToManyField(Labels, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
