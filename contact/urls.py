from django.conf.urls import url

from .views import (
        # Contact, 
        # Subscription,
        send_mail 
        )

urlpatterns = [
    url(r'^$', send_mail, name='contact'),
]

