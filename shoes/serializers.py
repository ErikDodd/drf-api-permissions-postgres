from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("owner", "name", "description", "laces", "brand", "color", "created_at")
        model = Shoe
