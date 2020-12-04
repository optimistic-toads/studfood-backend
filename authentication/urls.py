from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApi, UserApi
from rest_framework import routers

app_name = 'user'
router = routers.DefaultRouter()
router.register(r'user_crud', UserApi)

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('crud/', include(router.urls))
]
