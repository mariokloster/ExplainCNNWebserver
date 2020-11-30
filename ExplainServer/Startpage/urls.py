from django.urls import path
from Startpage import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
