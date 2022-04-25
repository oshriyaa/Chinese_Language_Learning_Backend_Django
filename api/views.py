from collections import Counter
from django.shortcuts import render, redirect
from api import models
from api.models import Category
from api.models import Vocabulary
# from api.models import User
from api.serializer import CategorySerializer,  VocabularySerializer, WordOfTheDaySerializer
from rest_framework import viewsets
from rest_framework import generics
import random

from favourite.serializers import FavouriteSerializer


# Create your views here.
class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class VocabularyView(viewsets.ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer


