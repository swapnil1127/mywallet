from django.conf.urls import url
from mywallet_biller.views import BillerDashboard


urlpatterns = [
    url(r'^biller/dashboard/', BillerDashboard.as_view(), name='mywallet_biller-dashboard'),
]
