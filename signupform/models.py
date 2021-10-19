from django.db import models

# Models go here
class SignupDetail(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField()