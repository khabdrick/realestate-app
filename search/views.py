from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from properties.models import Property #or whatever your model is


class SearchPropertyView(ListView):
    template_name = "page/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPropertyView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('location')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Property.objects.search(query)
        return Property.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''