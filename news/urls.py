from django.contrib import admin
from django.urls import path
from news import views


urlpatterns = [
    path('', views.news_list), # GET -> list, POST -> create
    path('<int:news_id>/', views.news_detail), # GET -> retrieve, PUT -> update, DELETE -> delete
    path('comments/', views.comment_list),
]
