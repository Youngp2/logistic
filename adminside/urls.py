from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name ='adminside'

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('order-list/',views.OrderList, name='order-list'),
    path('new-order/',views.NewOrder, name='new-order'),
    path('update-order/<str:pk>/',views.updateOrder, name='update-order'),
    path('details/<str:pk>/', views.details, name = 'details'),
    path('delete/<str:pk>/', views.deleteorder, name='delete-order'),
   
    path('alllmessages/',views.Allmessages, name='all-messages'),
    path('message-details/<str:pk>/', views.messageDetails, name = 'message-details'),
    path('delete/<str:pk>/', views.deletemessage, name='delete-message'),
    path('test/', views.status, name ='email')
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
