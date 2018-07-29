"""backend URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
import webapi.views as django_rest
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/(?P<pk>\d+)', django_rest.UserDetailView.as_view()),
    url(r'^user/', django_rest.UserView.as_view()),
    url(r'^employee/(?P<pk>\d+)', django_rest.EmployeeDetailView.as_view()),
    url(r'^employee/', django_rest.EmployeeView.as_view()),
    url(r'^contract/(?P<pk>\d+)', django_rest.EmployeeContractDetailView.as_view()),
    url(r'^contract/', django_rest.EmployeeContractView.as_view()),
    url(r'jwt-auth/', obtain_jwt_token),
    url(r'jwt-refresh/', refresh_jwt_token),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]