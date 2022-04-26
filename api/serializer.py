from rest_framework import serializers
from enroll.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('name','email','password')