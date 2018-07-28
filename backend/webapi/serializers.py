from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Employee, EmployeeContract


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'user', 'name', 'working_address', 'work_mobile',
                  'work_location', 'work_email', 'work_phone',
                  'public_info')


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    class Meta:
        model = User
        fields = ('username', 'employee')

    def create(self, validated_data):
        profile_data = validated_data.pop('employee')
        user = User.objects.create(**validated_data)
        Employee.objects.create(user=user, **profile_data)
        return user


class EmployeeContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContract
        fields = ('id', 'employee', 'job_title', 'dc_type', 'wage',
                  'salary_struct', 'tp_duration_begin', 'tp_duration_end',
                  'duration_begin', 'duration_end', 'schedule',
                  'pay_schedule', 'visa_no', 'visa_expiry', 'work_permit_no')