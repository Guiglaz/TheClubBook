from django.urls import path
from communitymanager import views


urlpatterns = [
    path('connecte', views.connecte, name='connected')

    ]