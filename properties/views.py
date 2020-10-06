# from django.views import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect

from .mixins import  ObjectViewedMixin


from .models import  Property



# class PropertyFeaturedListView(ListView):
#     template_name = "page/index.html"

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return Property.objects.all().featured()


# class PropertyFeaturedDetailView(ObjectViewedMixin, DetailView):
#     queryset = Property.objects.all().featured()
#     template_name = "property/featured-detail.html"

#     # def get_queryset(self, *args, **kwargs):
#     #     request = self.request
#     #     return Property.objects.featured(



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



class PropertyDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = Property.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PropertiesDetailSlugView, self).get_context_data(*args, **kwargs)
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

