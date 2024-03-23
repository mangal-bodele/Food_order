from django.urls import path
from .views import create_foodorder,show_foodorder,update_foodorder,cancel_foodorder

urlpatterns = [
    path('create/',create_foodorder,name='create_url'),
    path('show/',show_foodorder,name='show_url'),
    path('update/<int:pk>/',update_foodorder,name='update_url'),
    path('cancel/<int:pk>/',cancel_foodorder,name='cancel_url')
]