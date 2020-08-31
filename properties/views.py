from django.shortcuts import render
from django.views.generic import ListView

def property(request):
    context = {}
    return render(request,'index.html', context)