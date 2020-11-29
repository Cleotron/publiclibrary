from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    in_use = models.BooleanField()
    reservations = models.IntegerField()

    def __str__(self):
        return self.title
