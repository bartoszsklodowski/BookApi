import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from rest_framework import viewsets, status
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def db_create(request):
    if request.method == 'POST':
        Book.objects.all().delete()
        body = request.data
        q = body["q"]
        id = 1
        with urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q={q}') as response:
            data = json.load(response)
            for i in data["items"]:
                try:
                    title = i["volumeInfo"]["title"]
                except KeyError:
                    title = None
                try:
                    authors = i["volumeInfo"]["authors"]
                except KeyError:
                    authors = None
                try:
                    published_date = i["volumeInfo"]["publishedDate"]
                except KeyError:
                    published_date = None
                try:
                    categories = i["volumeInfo"]["categories"]
                except KeyError:
                    categories = None
                try:
                    average_rating = i["volumeInfo"]["averageRating"]
                except KeyError:
                    average_rating = None
                try:
                    ratings_count = i["volumeInfo"]["ratingsCount"]
                except KeyError:
                    ratings_count = None
                try:
                    thumbnail = i["volumeInfo"]["imageLinks"]["thumbnail"]
                except KeyError:
                    thumbnail = None
                Book.objects.create(id=id, title=title, authors=authors, published_date=published_date, categories=categories,
                                    average_rating=average_rating, ratings_count=ratings_count, thumbnail=thumbnail)
                id += 1

        return Response({"message": "Database updated"})


