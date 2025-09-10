from django.urls import path
from . import views
urlpatterns = [
    path("v1/", views.v1, name="app2-v1"),
    path("v2/", views.v2, name="app2-v2"),
]
