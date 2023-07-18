from django.urls import path
from accounts import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.UpdateProfile.as_view(), name='edit'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
