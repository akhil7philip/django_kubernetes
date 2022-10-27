from django.db import models

# Create your models here.
class PollsModel (models.Model):
    name = models.TextField(null=True, blank=True)