from django.db import models
from django.contrib.auth.models import User



class Singup(User):
    Address=models.CharField(max_length=200)

