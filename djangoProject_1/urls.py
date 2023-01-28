from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from eds.views.cat import root
from djangoProject_1 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('ad/', include('eds.urls.ad')),
    path('cat/', include('eds.urls.cat')),
    path('user/', include('users.urls')),
    path('selection/', include('eds.urls.selection')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
