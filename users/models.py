from django.db import models
from django.contrib.auth.models import AbstractUser, User


class BooksUser(AbstractUser):
    age = models.CharField(max_length=50)
    is_premium = models.BooleanField(default=False)

    following = models.ManyToManyField(
        'self', related_name="followers", symmetrical=False)
