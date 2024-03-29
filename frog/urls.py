"""frog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from web import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('change/', views.change, name='change'),
    path('register/', views.register, name='register'),
    path('Journalism/', views.Journalism, name='Journalism'),
    path('gyzf/', views.gyzf, name='gyzf'),
    path('zwz/', views.zwz, name='zwz'),
    path('mrt/', views.mrt, name='mrt'),
    path('jlb/', views.jlb, name='jlb'),
    path('luntan/', views.luntan, name='luntan'),
    path('develop/', views.develop, name='develop'),
]
