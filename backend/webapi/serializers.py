from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Employee, EmployeeContract


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user', 'name', 'working_address', 'work_mobile',
                  'work_location', 'work_email', 'work_phone',
                  'public_info')


class EmployeeContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContract
        fields = ('user', 'job_title', 'dc_type', 'wage',
                  'salary_struct', 'tp_duration_begin', 'tp_duration_end',
                  'duration_begin', 'duration_end', 'schedule',
                  'pay_schedule', 'visa_no', 'visa_expiry', 'work_permit_no')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email')

