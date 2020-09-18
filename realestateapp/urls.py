from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, RedirectView

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import LoginView, RegisterView
from .views import home_page, about_page


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page, name="home"),
    path('about', about_page, name="about"),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include("accounts.urls", namespace='account')),
    path('account/', include("accounts.passwords.urls")),
    path('contact/', include("contact.urls")),
<<<<<<< Updated upstream
    path('page/', include("page.urls")),
    path('properties/', include("properties.urls")),
=======
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('property/', include("Property.urls")),
>>>>>>> Stashed changes
    path('search/', include("search.urls")),


    path('', include('Property.urls')),
    # path('', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 