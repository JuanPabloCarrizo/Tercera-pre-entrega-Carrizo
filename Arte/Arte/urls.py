from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


handler404 = 'GaleriaApp.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Usuarios.urls')),
    path('', include('GaleriaApp.urls')),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

