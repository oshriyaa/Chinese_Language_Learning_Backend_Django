from urllib import request
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from api.models import Vocabulary
from favourite import models
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from rest_framework.generics import GenericAPIView

from favourite.serializers import FavouriteSerializer

# Post favourite
class FavouritePhrase(APIView):
    serializer_class = FavouriteSerializer
    
    def post(self, request, WordID,format=None):
        user_id = self.request.user.id
        if models.Favourite.objects.filter(vocabulary=WordID, user=user_id):              
            models.Favourite.objects.filter(vocabulary=WordID, user=user_id).delete()
            # return found if the data exists in database
            return HttpResponse('Found')
        else:     
            data = { 'user': user_id, 'vocabulary': WordID }
            serializer = FavouriteSerializer(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # return Notfound if the data doesn't exists in database
            return HttpResponse('NotFound')
        
# Get faourite Views
class GetFavouriteView(generics.ListAPIView):
    serializer_class = FavouriteSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        return models.Favourite.objects.filter(user=user_id).all()
