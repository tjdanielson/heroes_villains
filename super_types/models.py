from django.db import models

# Create your models here.
class SuperTypes(models.Model):
    type = models.CharField(max_length=50)