from django.urls import path

from .views import *


app_name = "anticafe"

urlpatterns = [
    path('clients/', ClientView.as_view()),
    path('clients/<int:pk>', SingleClientView.as_view()),
]
