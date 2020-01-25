from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/new_random', views.get_random_image_filepath),
]