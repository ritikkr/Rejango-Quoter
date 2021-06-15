'''
serializer are basically used to convert complext datatypes
to basic native python datatypes that can be easily rendered into json
'''
from django.db.models import fields
from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']