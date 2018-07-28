# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from webapi.models import Employee, EmployeeContract
from webapi.permissions import IsOwnerOrReadOnly, IsAdminOrDeny, IsOwnerOrDeny
from webapi.serializers import EmployeeSerializer, EmployeeContractSerializer


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


class EmployeeContractDetailView(CreateModelMixin, RetrieveUpdateAPIView):
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrDeny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeContractView(ListAPIView):
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAdminOrDeny,)