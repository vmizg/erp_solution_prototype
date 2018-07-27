"""anquan_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import django_rest.views as django_rest

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', django_rest.AllTech.as_view()),
    url(r'(?P<pk>\d+)', django_rest.TechView.as_view()),
    url(r'^crypt/', django_rest.Crypt.as_view())
]
