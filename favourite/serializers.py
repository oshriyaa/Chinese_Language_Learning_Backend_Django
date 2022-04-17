from favourite.models import Favourite
from rest_framework import serializers


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('id', 'user', 'vocabulary')