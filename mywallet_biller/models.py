# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MyWalletBiller(models.Model):
	name = models.CharField(max_length=100)
	passward = models.CharField(max_length=50)
	balance_amt = models.PositiveIntegerField(default=0)
	margin = models.PositiveIntegerField()
	active = models.IntegerField(default=1)
