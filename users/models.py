from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

class Role(models.Model):
    name = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.name

class User(AbstractUser):
    avatars = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField('Дата рождения', null=True)

    def __str__(self):
        return self.username

