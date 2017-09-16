from rest_framework import serializers
from .models import Pizza

class PizzaSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name','description')
        