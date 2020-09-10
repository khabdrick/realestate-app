from django.conf.urls import url

from .views import (
        _storey_building, 
        storey_building,
        bungalow,
        condo,
        duplex,
        flat,
        self_contain,
        )

app_name = 'page'

urlpatterns = [
    url(r'^2_storey_building/$', _storey_building, name='_storey_building'),
    url(r'^bungalow/$', bungalow, name='bungalow'),
    url(r'^condo/$', condo, name='condo'),
    url(r'^duplex/$', duplex, name='duplex'),
    url(r'^flat/$', flat, name='flat'),
    url(r'^self_contain/$', self_contain, name='self_contain'),
    url(r'^storey_building/$', storey_building, name='storey_building'),
]

