from django.conf.urls import url

from .views import (
        SearchPropertiesView
        )


urlpatterns = [
    url(r'^$', SearchPropertiesView.as_view(), name='query'),
]
