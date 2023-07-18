from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


class account(User):
    account_img = models.ImageField(upload_to='account_img')
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.username


