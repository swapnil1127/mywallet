# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from mywallet_users.models import MyWalletUser

# Create your views here.

class UserDashboard(View):
	'''
		This will be use for display User Dashboard
	'''

	def get(self, request):
		try:
			biller_list = MyWalletUser.objects.all()
		except Exception as e:
			print e

		return HttpResponse("Hi this is User Dashboard Page")

