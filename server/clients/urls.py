from django.urls import path

from .views import EmailView

urlpatterns = [
    path("test/", EmailView, name="email"),
]
