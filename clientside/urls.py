from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name='clientside'


urlpatterns = [
    path('', views.Home, name = 'homepage'),
    path('about/', views.About, name = 'about'),
    path('services/', views.Services, name = 'services'),
    path('track/', views.Track, name = 'track'),
    path('contact/', views.Contact, name = 'contact'),  
    
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

