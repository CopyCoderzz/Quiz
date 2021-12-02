"""QUIZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from MAIN.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('signin', views.signin, name='signin'),
    
    path('home/<pk>/', views.home,name='home'),
    path('view_user',views.view_user,name='view_user'),
    path('addQuestion/', views.addQuestion,name='addQuestion'),
    path('logoutPage/', views.logoutPage,name='logoutPage'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('showanswer/<pk>/', views.showanswer, name='showanswer'),

    path('college_reg',views.college_reg,name='college_reg'),
    path('college_signup',views.college_signup,name='college_signup'),

    path('upload_file1',views.upload_file1,name='upload_file1'),
    path('upload_file',views.upload_file,name='upload_file'),   
    path('open_question',views.open_question,name='open_question'),
    path('start/<pk>/',views.start,name='start'),
    # path('open_question1',views.open_question1,name='open_question1'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)