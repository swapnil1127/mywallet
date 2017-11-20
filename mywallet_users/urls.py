from django.conf.urls import url
from mywallet_users.views import UserDashboard


urlpatterns = [
    url(r'^user/dashboard/', UserDashboard.as_view(), name='mywallet_user-dashboard'),
]
