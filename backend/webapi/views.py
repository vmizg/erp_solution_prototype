# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from webapi.models import Employee, EmployeeContract
from webapi.permissions import IsOwnerOrReadOnly, IsAdminOrDeny, IsOwnerOrDeny
from webapi.serializers import EmployeeSerializer, EmployeeContractSerializer, UserSerializer


class EmployeeDetailView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class EmployeeView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class EmployeeContractDetailView(RetrieveUpdateAPIView):
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrDeny,)


class EmployeeContractView(ListAPIView):
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrDeny,)


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer