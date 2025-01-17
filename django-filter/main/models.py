from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=800)
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(to=Genre)

    def __str__(self):
        return self.title
