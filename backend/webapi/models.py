# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from encrypted_fields import *


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, default='')
    working_address = models.CharField(max_length=200, default='')
    work_mobile = models.CharField(max_length=12, default='')
    work_location = models.CharField(max_length=200, default='')
    work_email = models.EmailField(default='')
    work_phone = models.CharField(max_length=12, default='')
    public_info = models.CharField(max_length=400, default='')

    def __str__(self):
        return self.name


class EmployeeContract(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    job_title = EncryptedCharField(max_length=100, default='')
    dc_type = EncryptedCharField(max_length=50, default='')
    wage = EncryptedFloatField(default=0.0)
    salary_struct = EncryptedCharField(max_length=100, default='')
    tp_duration_begin = EncryptedDateField(default='')
    tp_duration_end = EncryptedDateField(default='')
    duration_begin = EncryptedDateField(default='')
    duration_end = EncryptedDateField(default='')
    schedule = EncryptedIntegerField(default=0) # days / week
    pay_schedule = EncryptedIntegerField(default=0) # corresponding to pay type (0 - monthly, 1 - weekly, etc)
    visa_no = EncryptedCharField(max_length=50, default='')
    visa_expiry = EncryptedDateField(default='')
    work_permit_no = EncryptedCharField(max_length=50, default='')

    def __str__(self):
        return str(self.employee)



