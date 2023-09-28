from django.urls import path
from users import views


urlpatterns = [
    path('users/login/', views.Login.as_view()),
    path('users/register/', views.register),
    path('users/logout/', views.logout),
    path('users/profile/', views.profile),
]
