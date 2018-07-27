# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from django_rest.models import Employee, EmployeeContract, EmployeeWorkPermit
from django_rest.serializer import EmployeeSerializer, EmployeeContractSerializer, EmployeeWorkPermitSerializer


class EmployeeDetailView(APIView):

    def get(self, request, pk, format=None):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ContractView(viewsets.ModelViewSet):
    queryset = EmployeeContract.objects.all()
    serializer_class = EmployeeContractSerializer


class WorkPermitView(viewsets.ModelViewSet):
    queryset = EmployeeWorkPermit.objects.all()
    serializer_class = EmployeeWorkPermitSerializer