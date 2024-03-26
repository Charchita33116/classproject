from django.db import models


class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)

# Create your models here.