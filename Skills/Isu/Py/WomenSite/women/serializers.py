from rest_framework import serializers
from django.contrib.auth.models import User
#from .models import Women
#class WomenSerializer(serializers.ModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
#    class Meta:
#        model = Women
#        fields = ['id', 'title', 'content', 'owner']
class UserSerializer(serializers.ModelSerializer):
#    womens = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username']