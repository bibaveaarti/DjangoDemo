from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("New Application")

def student(request):
    return HttpResponse("Welcome BVIMIT")
