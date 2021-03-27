from django.urls import path
from .views import ClientView


app_name = "anticafe"

urlpatterns = [
    path('clients/', ClientView.as_view()),
]