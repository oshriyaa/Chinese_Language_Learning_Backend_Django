from unittest import result
from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User

USER_TYPES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')
)

from api.models import Vocabulary
# Create your models here.
User = settings.AUTH_USER_MODEL

class UserResults(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    testDate = models.CharField(max_length=20)
    testTime = models.CharField(max_length=20)
    level = models.CharField(max_length=10)
    result = models.IntegerField()
    
    objects = models.Manager()