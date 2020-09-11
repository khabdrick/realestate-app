from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect



def _storey_building(request):
    return render(request, "page/2_storey_building.html")

def storey_building(request):
    return render(request, "page/storey_building.html")

def bungalow(request):
    return render(request, "page/bungalow.html")

def condo(request):
    return render(request, "page/condo.html")

def duplex(request):
    return render(request, "page/duplex.html")

def flat(request):
    return render(request, "page/flat.html")

def self_contain(request):
    return render(request, "page/self_contain.html")
