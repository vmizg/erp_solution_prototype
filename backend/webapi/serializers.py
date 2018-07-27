from rest_framework import serializers
from .models import Employee, EmployeeContract, EmployeeWorkPermit


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'working_address', 'work_mobile',
                  'work_location', 'work_email', 'work_phone',
                  'public_info')


class EmployeeContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContract
        fields = ('id', 'name', 'job_title', 'dc_type', 'wage',
                  'salary_struct', 'tp_duration_begin', 'tp_duration_end',
                  'duration_begin', 'duration_end', 'schedule',
                  'pay_schedule')


class EmployeeWorkPermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkPermit
        fields = ('id', 'name', 'visa_no', 'visa_expiry', 'work_permit_no')