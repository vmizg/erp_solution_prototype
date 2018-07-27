# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from encrypted_fields import *


class Employee(models.Model):
    name = models.CharField(max_length=100)
    working_address = models.CharField(max_length=200)
    work_mobile = models.CharField(max_length=12)
    work_location = models.CharField(max_length=200)
    work_email = models.EmailField()
    work_phone = models.CharField(max_length=12)
    public_info = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class EmployeeContract(models.Model):
    name = models.OneToOneField(Employee)

    job_title = EncryptedCharField(max_length=100)
    dc_type = EncryptedCharField(max_length=50)
    wage = EncryptedFloatField()
    salary_struct = EncryptedCharField(max_length=100)
    tp_duration_begin = EncryptedDateField()
    tp_duration_end = EncryptedDateField()
    duration_begin = EncryptedDateField()
    duration_end = EncryptedDateField()
    schedule = EncryptedIntegerField() # days / week
    pay_schedule = EncryptedIntegerField() # corresponding to pay type (0 - monthly, 1 - weekly, etc)

    def __str__(self):
        return self.name


class EmployeeWorkPermit(models.Model):
    name = models.OneToOneField(EmployeeContract)

    visa_no = EncryptedCharField(max_length=50)
    visa_expiry = EncryptedDateField()
    work_permit_no = EncryptedCharField(max_length=50)

    def __str__(self):
        return self.name




