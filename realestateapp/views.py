from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect

from properties.models import Property


def home_page(request):
    object_list = Property.objects.all().featured()
    context = {
        "object_list": object_list,
    }
    return render(request, 'index.html', context)


def about_page(request):
    return render(request, "about.html")
