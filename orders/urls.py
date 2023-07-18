from django.urls import path
from django.conf.urls import url
from orders import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
app_name = 'orders'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^create/$', views.order_create, name='order_create'),
    path('update_order/<int:id>/', views.updateOrder, name="update_order"),
    path('load-cities/', views.load_cities, name='ajax_load_cities'),
]
