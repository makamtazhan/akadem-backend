from django.urls import path
from api import views

urlpatterns = [
    path('major/', views.majors),
    path('status/', views.statuses),
]