from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
<<<<<<< Updated upstream
from properties.models import Properties #or whatever your model is
=======
from Property.models import Property #or whatever your model is
>>>>>>> Stashed changes


class SearchPropertiesView(ListView):
    template_name = "page/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPropertiesView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('location')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Properties.objects.search(query)
        return Properties.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''