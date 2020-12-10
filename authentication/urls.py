from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi, UserApi


app_name = 'user'

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('crud/', UserApi.as_view(), name='user')
]
