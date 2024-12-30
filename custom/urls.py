from django.contrib import admin
from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
    path('home/',home,name='home'),
    path('order/',order,name='order'),
    path('product',product,name='product'),
    path('delete/<id>/', delete, name = "delete"),
    path('update/<id>/', update, name = "update"),
    path('delete_product/<id>/',delete_product, name = "delete_product"),
    path('update_product/<id>/', update_product, name = "update_product"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)