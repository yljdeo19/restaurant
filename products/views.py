import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy, utils

from products import models, forms, mixins
from products.forms import products
from products.models import Product, Category, Post
from cart.forms import CartAddProductForm
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from django.db.models import Q
from django.views.generic import TemplateView, ListView


@method_decorator(allowed_users(allowed_roles=['Administrator']), name='dispatch')
class create(generic.CreateView):
    model = models.Product
    form_class = forms.products
    template_name = 'product.html'
    extra_context = {'post_form': form_class}
    success_url = reverse_lazy('index')


class production():
    model = models.Product
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)

    def __init__(self):
        self.GET = None

    def category(request, category_slug=None):
        product = Product.objects.filter(available=True)
        category = None
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            product = product.filter(category=category)

        return render(request,
                      'list.html',
                      {'category': category,
                       'categories': categories,
                       'products': product})

    def product_list(request, category_slug=None):
        categories = Category.objects.all()
        product = Product.objects.filter(available=True)
        paginator = Paginator(product, 8)
        page = request.GET.get('page')
        product = paginator.get_page(page)
        return render(request,
                      'list.html',
                      {'categories': categories, 'products': product})


def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.category = request.POST.get("category")
            product.name = request.POST.get("name")
            product.description = request.POST.get("description")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'product_detail.html', context)


class ProductListView(ListView):
    model = models.Product
    template_name = 'Search.html'
    categories = Category.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            queryset = self.model.objects.filter(
                Q(name__icontains=query[0].upper()) |
                Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)

        return context
