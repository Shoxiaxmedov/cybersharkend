"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('compyuters/', views.compyuters, name="compyuters"),
    path('cs-go2/', views.cs_go, name="cs-go"),
    path('dota2/', views.dota2, name="dota2"),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('index/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('turnir/', views.turnir, name="turnir"),
    path('compyuter1', views.compyuter1, name="compyuter1"),
    path('compyuter2', views.compyuter2, name="compyuter2"),
    path('compyuter3', views.compyuter3, name="compyuter3"),
    path('compyuter4', views.compyuter4, name="compyuter4"),
    path('user_logout/', views.user_logout, name='logout'),
    # path('dashboard/', views.dashboard, name="dashboard"),
    path('compyuterzone/', views.compyuterzone, name='compyuterzone'),
    path('check_user_exists/', views.check_user_exists, name='check_user_exist'),
    path('profile_new/', views.profile_create, name='profile_create'),
    path('profile/', views.profile_list, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
