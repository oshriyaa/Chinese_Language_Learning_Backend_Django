from unittest import result
from urllib import request
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import generics
from results.models import UserResults
# from api.models import Vocabulary
from users import models
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

from results.serializers import ResultsSerializer

# Create your views here.

# @csrf_exempt
class UserResultsData(APIView):
    

    serializer_class = ResultsSerializer

    def post(self, request, format=None):

        user_id = self.request.user.id
        
        data = { 'user': user_id,'testDate': request.data['testDate'],'testTime' : request.data['testTime'], 'level': request.data['level'], 'result':request.data['result'] }
        serializer = ResultsSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse('NotFound')
        

class GetResultsView(generics.ListAPIView):
    serializer_class = ResultsSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        return UserResults.objects.filter(user=user_id).all()

