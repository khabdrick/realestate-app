# from django.views import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect

from .mixins import  ObjectViewedMixin


from .models import  Properties



# class PropertyFeaturedListView(ListView):
#     template_name = "page/index.html"

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return Property.objects.all().featured()


# class PropertyFeaturedDetailView(ObjectViewedMixin, DetailView):
#     queryset = Property.objects.all().featured()
#     template_name = "Property/featured-detail.html"

#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     return Property.objects.featured(



<<<<<<< Updated upstream:properties/views.py
class PropertiesListView(ListView):
    template_name = "properties/property.html"
=======
class PropertyListView(ListView):
    template_name = "Property/property.html"
>>>>>>> Stashed changes:Property/views.py

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyListView, self).get_context_data(*args, **kwargs)
        return context
    

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Property.objects.all()


def Property_list_view(request):
    queryset = Property.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, "Property/property.html", context)



class PropertiesDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = Properties.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PropertyDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Property.objects.get(slug=slug, active=True)
        except Property.DoesNotExist:
            raise Http404("Not found..")
        except Property.MultipleObjectsReturned:
            qs = Property.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


def _storey_building(request):
    object_list         = Properties.objects.filter(property_type='2 Storey Building')
    context             = {
        "object_list": object_list
    }
    return render(request, "properties/2_storey_building.html")

def storey_building(request):
    return render(request, "properties/storey_building.html")

def bungalow(request):
    object_list         = Properties.objects.filter(property_type='Bungalow')
    context             = { 
        "object_list": object_list
    }
    return render(request, "properties/bungalow.html", context)

def condo(request):
    object_list         = Properties.objects.filter(property_type='Condo')
    context             = { 
        "object_list": object_list
    }
    return render(request, "properties/condo.html", context)

def duplex(request):
    object_list         = Properties.objects.filter(property_type='Duplex')
    context             = { 
        "object_list": object_list
    }
    return render(request, "properties/duplex.html", context)

def flat(request):
    object_list         = Properties.objects.filter(property_type='Flat')
    context             = { 
        "object_list": object_list
    }
    return render(request, "properties/flat.html", context)

def self_contain(request):
    object_list         = Properties.objects.filter(property_type='Self Contain')
    context             = { 
        "object_list": object_list
    }
    return render(request, "properties/self_contain.html", context)

# import os
# from wsgiref.util import FileWrapper # this used in django
# from mimetypes import guess_type

# from django.conf import settings


# class PropertiesDetailView(ObjectViewedMixin, DetailView):
#     #queryset = Properties.objects.all()
#     template_name = "properties/property_details.html"

#     def get_context_data(self, *args, **kwargs):
#         context = super(PropertiesDetailView, self).get_context_data(*args, **kwargs)
#         print(context)
#         # context['abc'] = 123
#         return context

#     def get_object(self, *args, **kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         instance = Properties.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Properties doesn't exist")
#         return instance

#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     pk = self.kwargs.get('pk')
#     #     return Properties.objects.filter(pk=pk)


# def Properties_detail_view(request, pk=None, *args, **kwargs):
#     # instance = Properties.objects.get(pk=pk, featured=True) #id
#     # instance = get_object_or_404(Properties, pk=pk, featured=True)
#     # try:
#     #     instance = Properties.objects.get(id=pk)
#     # except Properties.DoesNotExist:
#     #     print('no Properties here')
#     #     raise Http404("Properties doesn't exist")
#     # except:
#     #     print("huh?")

#     instance = Properties.objects.get_by_id(pk)
#     if instance is None:
#         raise Http404("Properties doesn't exist")
#     #print(instance)
#     # qs  = Properties.objects.filter(id=pk)

#     # #print(qs)
#     # if qs.exists() and qs.count() == 1: # len(qs)
#     #     instance = qs.first()
#     # else:
#     #     raise Http404("Properties doesn't exist")

#     context = {
#         'object': instance
#     }
#     return render(request, "properties/property_details.html", context)
