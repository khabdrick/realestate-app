from django.conf.urls import url

from .views import (
        SearchPropertyView
        )


urlpatterns = [
    url(r'^$', SearchPropertyView.as_view(), name='query'),
]
