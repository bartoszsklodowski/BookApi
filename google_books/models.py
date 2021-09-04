from django.db import models


class Book(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    authors = models.CharField(max_length=50, null=True)
    published_date = models.CharField(max_length=10, null=True)
    categories = models.CharField(max_length=50, null=True)
    average_rating = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.title} {self.authors}"


# {
#     "title": "Hobbit czyli Tam i z powrotem",
#     "authors": ["J. R. R. Tolkien"],
#     "published_date": "2004",
#     "categories": [
#         "Baggins, Bilbo (Fictitious character)"
#       ],
#     "average_rating": 5,
#     "ratings_count": 2,
#     "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
# }