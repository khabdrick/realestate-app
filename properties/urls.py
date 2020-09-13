from django.urls import path,re_path

from .views import (
        PropertiesListView, 
        PropertiesDetailSlugView,
        )


urlpatterns = [
    path('', PropertiesListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', PropertiesDetailSlugView.as_view(), name='detail'),
    
]

