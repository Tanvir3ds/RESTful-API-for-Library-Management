from django.contrib import admin
from django.urls import path, include

# import static & media setting
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_app.urls')),
    path('api/', include('api.urls')),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
