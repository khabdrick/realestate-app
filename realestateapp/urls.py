from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, about_page


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page, name="home"),
    path('about', about_page, name="about"),
    # path('blog/', include("blog.urls")),
    path('contact/', include("contact.urls")),
    path('page/', include("page.urls")),
    path('properties/', include("properties.urls")),
    path('search/', include("search.urls")),


    path('', include('properties.urls')),
    # path('', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 