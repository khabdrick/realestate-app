from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

<<<<<<< Updated upstream
from properties.models import Properties
=======
from Property.models import Property
>>>>>>> Stashed changes


def home_page(request):
	object_list = Properties.objects.all().featured()
	context 	= {
		"object_list": object_list,
	}
	return render(request, 'page/index.html', context)
    

def about_page(request):
    return render(request, "page/about.html")




