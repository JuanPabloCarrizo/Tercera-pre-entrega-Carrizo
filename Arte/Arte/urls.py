from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Usuarios import views


handler404 = 'Usuarios.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Usuarios.urls')),
    path('', include('GaleriaApp.urls')),        
    # para cuando entren en una dirección que no existe
    path('page-not-found/', views.page_not_found),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

