from django.urls import path

from .views import *

urlpatterns = (
    path("document/",    DocumentAPIView.as_view()),
    path("client/",      ClientAPIView.as_view())
)
