from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Panorama Hotel'
admin.site.index_title = 'Reception of Panorama Hotel'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotelbooking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
