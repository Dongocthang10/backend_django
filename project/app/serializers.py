from rest_framework import serializers
from .models import Model

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"