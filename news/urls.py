from django.contrib import admin
from django.urls import path
from news import views


urlpatterns = [
    path('news/', views.news_list), # GET -> list, POST -> create
    path('<int:news_id>/', views.news_detail), # GET -> retrieve, PUT -> update, DELETE -> delete
    path('comments/', views.comment_list),
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('tags/', views.TagViewSet.as_view(
        {'get': 'list', 'post': 'create'}
        )),
    path('tags/<int:id>/', views.TagViewSet.as_view(
        {'get': 'retrieve'}
        )),
]
