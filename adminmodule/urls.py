"""ngo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login",views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    path('addadmin', views.addadmin, name='addadmin'),
    path('branch', views.branch, name='branch'),
    path('deleteinstance', views.deleteinstance, name='deleteinstance'),
    path('activatebranch',views.activatebranch,name='activatebranch'),
    path('member', views.member, name='member'),
    path('updatemember', views.updatemember, name='updatemember'),
    path('memberpost', views.memberpost, name='memberpost'),

    path('org', views.org, name='org'),
    path('updateorg', views.updateorg, name='updateorg'),
    path('campaign', views.campaign, name='campaign'),
    path('viewcamp', views.viewcamp, name='viewcamp'),
    path('changepass', views.changepass, name='changepass'),
    path('showdonations', views.showdonations, name='showdonations'),
    path('showusers', views.showusers, name='showusers'),

]
