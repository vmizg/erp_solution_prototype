from rest_framework import serializers
from .models import Tech, TestCrypt


class TechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tech
        fields = '__all__'


class TestCryptSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestCrypt
        fields = '__all__'
