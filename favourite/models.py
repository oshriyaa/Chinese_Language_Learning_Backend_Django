from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User



from api.models import Vocabulary
# Create your models here.
User = settings.AUTH_USER_MODEL

class Favourite(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    word = models.ForeignKey(Vocabulary, default=1, null=True, on_delete=models.CASCADE)
    
    objects = models.Manager()