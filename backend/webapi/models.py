# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from encrypted_fields import *

from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    working_address = models.CharField(max_length=200, default='')
    work_mobile = models.CharField(max_length=12, default='')
    work_location = models.CharField(max_length=200, default='')
    work_email = models.EmailField(default='')
    work_phone = models.CharField(max_length=12, default='')
    public_info = models.CharField(max_length=400, default='')

    def __str__(self):
        return str(self.user)


class EmployeeContract(models.Model):
    user = models.OneToOneField(User, primary_key=True)

    job_title = EncryptedCharField(max_length=100, default='')
    dc_type = EncryptedCharField(max_length=50, default='')
    wage = EncryptedFloatField(default=0.0)
    salary_struct = EncryptedCharField(max_length=100, default='')
    tp_duration_begin = EncryptedDateField(null=True, blank=True)
    tp_duration_end = EncryptedDateField(null=True, blank=True)
    duration_begin = EncryptedDateField(null=True, blank=True)
    duration_end = EncryptedDateField(null=True, blank=True)
    schedule = EncryptedIntegerField(default=0) # days / week
    pay_schedule = EncryptedIntegerField(default=0) # corresponding to pay type (0 - monthly, 1 - weekly, etc)
    visa_no = EncryptedCharField(max_length=50, default='')
    visa_expiry = EncryptedDateField(null=True, blank=True)
    work_permit_no = EncryptedCharField(max_length=50, default='')

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This method will be called after creating a User instance
    (either from admin panel or implemented as a registration form later on)
    to create templates for User's Employee and EmployeeContract data.
    """
    if created:
        Employee.objects.create(user=instance)
        EmployeeContract.objects.create(user=instance)




