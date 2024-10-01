

from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField('Описание')
    done = models.BooleanField('Выполнено', default=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return self.name
