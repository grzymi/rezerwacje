from django.shortcuts import render
from django.http import HttpResponse
from .models import Audio

def index(request):
    question = Audio.objects.all()
    return HttpResponse(question)

# Create your views here.
