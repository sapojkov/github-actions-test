from django.urls import path
from .views import GreetingView

urlpatterns = [
    path("api/v1/greet/", GreetingView.as_view(), name="greet"),
]
