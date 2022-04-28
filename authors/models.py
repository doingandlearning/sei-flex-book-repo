from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name}"
