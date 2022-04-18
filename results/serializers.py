from results.models import UserResults
from rest_framework import serializers


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResults
        fields = ('id', 'user', 'testDate', 'testTime', 'level', 'result')