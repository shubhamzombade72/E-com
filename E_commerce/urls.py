"""
URL configuration for E_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from E_com_app import views
from django.conf import settings
from django.conf.urls.static import static
from E_commerce import ProductView
from E_commerce import OrderView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage), 


    
    path('product-list/', ProductView.product1),
    path('product-add/', ProductView.add_product, name='product-add'),
    path('product-view/<id>', ProductView.product_view),
    path('product-delete/<id>',ProductView.delete_product),
    path('product-edit/<id>', ProductView.edit_product),


    path('order-list/', OrderView.order_view),
    path('order-add/', OrderView.add_order),
    path('order-view/<id>', OrderView.view_order),
    path('order-edit/<id>', OrderView.edit_order),
    path('order-delete/<id>',OrderView.delete_order)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    