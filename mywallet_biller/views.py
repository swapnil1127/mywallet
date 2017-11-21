# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import View
from mywallet_biller.models import MyWalletBiller
from mywallet.settings import BASE_DIR

# Create your views here.

class BillerDashboard(View):
	'''
		This will be use for display Biller Dashboard
	'''
	template_path = 'user_dashboard.html'

	def dispatch(self, request, *args, **kwargs):
		return super(BillerDashboard, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		try:
			biller_list = MyWalletBiller.objects.all()
		except Exception as e:
			print e

		return render(request, self.template_path,{'data':"Hello"} )
		# return HttpResponse("Hi this is Biller Dashboard Page")

	def post(self, request):
		return True

class index(View):
	template_path = 'base.html'

	def dispatch(self, request, *args, **kwargs):
		return super(index, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_path, {})

	# return HttpResponse("Hi this is Biller Dashboard Page")

	def post(self, request):
		return True
