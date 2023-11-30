from django.db import models


class Author(models.Model):
    """Модель автора книги."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def str(self):
        return self.name


class Book(models.Model):
    """Модель книги."""

    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def str(self):
        return self.title
