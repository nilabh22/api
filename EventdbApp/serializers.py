from django.db.models import fields
from rest_framework import serializers
from EventdbApp.models import Winner, Prize, Location, Rules, Events

class WinnerSearializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'
        depth =1

class PrizeSearializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'
        depth =1
        

class LocationSearializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        depth =1

class RuleSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rules
        fields = '__all__'
        depth =1

class EventSearializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth =2