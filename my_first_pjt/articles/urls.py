from django.urls import path
from articles import views

urlpatterns = [
    path('data_throw/', views.data_throw, name="data_throw"),
    path('data_catch/', views.data_catch, name="data_catch"),
    
    path('', views.articles, name="articles"),
    path('create/', views.create, name="create"),
    path('new/', views.new_article, name="new_article"),
    
]