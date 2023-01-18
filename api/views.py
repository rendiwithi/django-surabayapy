from django.shortcuts import render
from rest_framework.decorators import api_view
from . import models
# Create your views here.


@api_view(['GET'])
def test(request):
    events = models.Event.objects.all()
    return events
