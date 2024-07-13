"""
URL configuration for LMS project.

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
from django.conf import settings
from django.urls import path,include
from .import views,user_login
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base/',views.BASE,name='base'),

    path('',views.HOME,name='home'),

    path('courses/',views.SINGLE_COURSE,name="single_course"),

    path('contact/',views.CONTACT_US,name="contact_us"),

    path('about/',views.ABOUT_US,name="about"),

    path('accounts/',include('django.contrib.auth.urls')),

    path('accounts/register/',user_login.REGISTER,name='register'),

    path('doLogin/',user_login.DOLOGIN,name='doLogin'),

    path('accounts/profile/',user_login.PROFILE,name='profile'),

    path('accounts/profile/update',user_login.PROFILE_UPDATE,name="profile_update"),

    path('courses/filter-data',views.filter_data,name="filter-data"),

    path('search',views.SEARCH_COURSE,name="search_course"),

    path('course/<slug:slug>',views.COURSE_DETAILS,name="course_details"),

    path('404',views.PAGE_NOT_FOUND,name="404"),

    path('checkout/<slug:slug>',views.CHECKOUT,name='checkout'),

    path('my-course',views.MY_COURSE,name="my_course"),

    path('verify_payment',views.VERIFY_PAYMENT,name='verify_payment'),

    path('course/watch-course/<slug:slug>',views.WATCH_COURSE,name='watch_course'),

    path('logout/', user_login.LOGOUT, name='logout'),

]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
