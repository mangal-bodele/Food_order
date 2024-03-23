from django.urls import path
from .views import signup_user,login_user,logout_user,change_pass

urlpatterns = [
    path('signup/',signup_user, name='signup_url'),
    path('login/',login_user, name='login_url'),
    path('logout/',logout_user, name='logout_url'),
    path('change/',change_pass, name='change_url')
]