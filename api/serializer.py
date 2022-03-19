import imp
from rest_framework import serializers

from api.models import Category, User
from api.models import Vocabulary


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
        'UserID',
        'UserFullName',
        'PhoneNumber',
        'Email',
        'Password',
        ]
