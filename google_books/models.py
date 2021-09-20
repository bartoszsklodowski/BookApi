from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    authors = models.CharField(max_length=255, null=True)
    published_date = models.CharField(max_length=255, null=True)
    categories = models.CharField(max_length=255, null=True)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.title} {self.authors}"