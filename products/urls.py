from django.urls import path
from . import views

app_name = 'dishes'

urlpatterns = [
    path('', views.ProductsList.as_view(), name='dishes_list')
]
