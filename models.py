from django.db import models

class adminLogin(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
