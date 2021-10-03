from rest_framework import routers
from django.urls import path, include
from .views import BookViewSet, db_create

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('db/', db_create, name='db'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]