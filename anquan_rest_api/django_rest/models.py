# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from encrypted_fields import EncryptedTextField

# Create your models here.


class Tech(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=200)


class TestCrypt(models.Model):
    uncrypted_text = models.CharField(max_length=200)
    crypted_text = EncryptedTextField()
