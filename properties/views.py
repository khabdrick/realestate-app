# from django.views import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from .mixins import  ObjectViewedMixin
from .models import  Property
from .forms import  PropertyForm

class PropertyListView(ListView):
    template_name = "properties/property.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PropertiesListView, self).get_context_data(*args, **kwargs)
        return context
    

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Properties.objects.all()


def Properties_list_view(request):
    queryset = Properties.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "properties/property.html", context)




def createproperty(request):
    form = PropertyForm()
    context = {
        'form': form
    }
    return render(request, 'properties/propertyform.html', context )