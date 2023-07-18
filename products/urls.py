from django.urls import path
from django.conf.urls import url
from products import views
from django.contrib.auth import views as auth_views
app_name = 'products'

urlpatterns = [
    path('add/', views.create.as_view(), name='adding'),
    path('', views.production.product_list, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('search/', views.ProductListView.as_view(), name='search'),
    path('detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.production.category, name='product_list_by_category'),

]
