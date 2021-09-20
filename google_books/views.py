import json
import urllib.request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .serializers import BookSerializer


class BookFilter(FilterSet):
    published_date = CharFilter(lookup_expr='icontains')
    authors = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['published_date', 'authors']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['published_date']


@api_view(['GET', 'POST'])
def db_create(request):
    if request.method == 'GET':
        return Response({"message": "You can here add records to database by pass q parameter"})
    if request.method == 'POST':
        body = request.data
        q = body["q"]
        url = "https://www.googleapis.com/books/v1/volumes?q=" + urllib.parse.quote(q)
        with urllib.request.urlopen(url) as response:
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
                Book.objects.create(title=title, authors=authors, published_date=published_date,
                                    categories=categories,
                                    average_rating=average_rating, ratings_count=ratings_count, thumbnail=thumbnail)

        return Response({"message": "Database updated"})
