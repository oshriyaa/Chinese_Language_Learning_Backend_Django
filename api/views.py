from django.shortcuts import render, redirect
from api.models import Category
from api.models import Vocabulary
from api.models import User
from api.serializer import CategorySerializer, UserSerializer, VocabularySerializer
from rest_framework import viewsets
from rest_framework import generics

from favourite.serializers import FavouriteSerializer


# Create your views here.
class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Vocabulary(viewsets.ModelViewSet):
    # search_fields = ['$InEnglish']
    # filter_backend = (filter.SearchFilter,)
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer


class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer