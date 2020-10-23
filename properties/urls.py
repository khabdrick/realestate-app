from django.urls import path,re_path

from .views import (
        PropertyListView, 
        # PropertyDetailSlugView,
        createproperty,
        )


urlpatterns = [
    path('', PropertyListView.as_view(), name='list'),
    # re_path(r'^(?P<slug>[\w-]+)/$', PropertyDetailSlugView.as_view(), name='detail'),
    path('createproperty/', createproperty, name='propertyform' ),
    
]
