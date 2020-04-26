from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('major/', views.majors),
    path('status/', views.statuses),
    path('program/', views.ProgramV.as_view()),
    path('program/<int:id>/', views.ProgramDV.as_view()),
    path('login/', obtain_jwt_token)
]