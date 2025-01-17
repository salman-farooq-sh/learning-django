from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=Category)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=12.34)

    @property
    def foo_dict(self):
        return {'x': 1, 'y': 'abc'}

    def __str__(self):
        return str(self.title)
