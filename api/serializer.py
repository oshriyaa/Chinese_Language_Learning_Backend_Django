from rest_framework import serializers
from .models import *
import random



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
        'CategoryID',
        'CategoryName',
        ]

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = [
        'WordID',
        'CategoryID',
        'InEnglish',
        'InNepali',
        'InChinese',
        'InPinYin',
        'InDevnagari',
        'Audio',
        ]

class WordOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = [
        'WordID',
        'CategoryID',
        'InEnglish',
        'InNepali',
        'InChinese',
        'InPinYin',
        'InDevnagari',
        'Audio',
        ]
