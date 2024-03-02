"""
URL configuration for secondTest project.

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
from django.urls import path,re_path
from secondTest.views import hour_offset,current_datetime,name_display
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    #(r'^now/$', current_datetime),
    path("admin",admin.site.urls),
    path('now/',current_datetime),
    #(r'^now/(plus|minus)(\d{1,2})hours/$', hour_offset),
    # use angle brackets to capture values.
    path('name/<str:name>/', name_display),
    # to work with regexes use the re_path
    # always use named queries to avoid confusion, note that you can use the previous style except that it's pretty redundant.
    re_path('now/(?P<direction>plus|minus>)(?P<hours>\d{1,2})hours/$', hour_offset),
]
