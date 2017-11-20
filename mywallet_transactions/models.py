# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MyWalletTransactions(models.Model):
	transaction_amt = models.IntegerField()  # for credit positive value, for debit negative value
	transaction_type = models.IntegerField()  # 1 - user to user, 2 - user added into wallet, 3- user to biller, 4 - Biller to admin
	balance_amt = models.PositiveIntegerField(default=0)
	to_user = models.IntegerField()
	to_user_type = models.IntegerField(default=3)  #1-admin, 2- biller , 3 -user
	from_user = models.IntegerField()
	from_user_type = models.IntegerField(default=3)  #1-admin, 2- biller , 3 -user

