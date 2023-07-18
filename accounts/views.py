from pyexpat.errors import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from orders.models import Order
from restaurant import views
from restaurant.views import index
from accounts import models, forms
from products.models import Product, Category
from .decorators import unauthenticated_user, allowed_users
from .forms import ContactForm, ProfileEditForm, UserProfileForm
from .models import account
from django.core.paginator import Paginator


def profile(request):
    orders = Order.objects.all()

    context = {
        'orders': orders,
    }
    return render(request, 'profile.html', context)


@method_decorator(allowed_users(allowed_roles=['Administrator']), name='dispatch')
class UserCreateView(generic.CreateView):
    model = models.account
    form_class = forms.UserProfileForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'loges.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


class UpdateProfile(generic.UpdateView):
    model = account
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile')
    template_name = 'update.html'

    def get_object(self):
        return self.request.user
