from django.urls import path
from mcp_core import views


urlpatterns = [
    path('', views.index)
]
