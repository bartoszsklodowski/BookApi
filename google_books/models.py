from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=True)
    authors = models.TextField(null=True)
    published_date = models.TextField(null=True)
    categories = models.TextField(null=True)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.TextField(null=True)

    def __str__(self):
        return f"{self.title} {self.authors}"
