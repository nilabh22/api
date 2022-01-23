import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.utils import json
from EventdbApp.models import Winner, Prize, Location, Rules, Events
from EventdbApp.serializers import WinnerSearializer,PrizeSearializer,LocationSearializer,RuleSearializer,EventSearializer

# Create your views here.

@csrf_exempt
def eventApi(request, id =1):
    if request.method =="GET":
        events = Events.objects.all()
        events_serializer = EventSearializer(events, many=True)
        return JsonResponse(events_serializer.data,safe = False)
    elif request.method =="POST":
        event_data = JSONParser().parse(request)
        events_serializer = EventSearializer(data = event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse(events_serializer.data, status="Added Succesfully", safe =False)
        return JsonResponse("Failed to Add",safe= False)


