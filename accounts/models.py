from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    # name = models.CharField(max_length=250, verbose_name='fish')
    # image = models.ImageField(verbose_name="photo", upload_to="mainapp/photo/%Y/%m/%d/", null=True, blank=True)
