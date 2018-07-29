# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from webapi.models import Employee, EmployeeContract
from webapi.permissions import IsOwnerOrReadOnly, IsAdminOrDeny, IsOwnerOrDeny, IsUserOwnerOrDeny
from webapi.serializers import EmployeeSerializer, EmployeeContractSerializer, UserSerializer


class EmployeeDetailView(RetrieveUpdateAPIView):
    """
    View selected employee public data.
    Permissions: owner: view & edit, everyone else: view
    Only possible to update data through the HTTP PUT form below
    while the Angular form is not implemented.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class EmployeeView(ListAPIView):
    """
    View employees.
    Permissions: everyone: view.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class EmployeeContractDetailView(RetrieveUpdateAPIView):
    """
    View selected employee contract data.
    Permissions: owner: view & edit, admin: view.
    Only possible to update data through the HTTP PUT form below
    while the Angular form is not implemented.
    """
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrDeny,)


class EmployeeContractView(ListAPIView):
    """
    View employee contracts.
    Permissions: admin: view.
    """
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrDeny,)


class UserDetailView(RetrieveAPIView):
    """
    View authenticated user data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)


class UserView(ListAPIView):
    """
    View users.
    Permissions: everyone: view.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

