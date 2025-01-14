from django.urls import path
from articles import views

urlpatterns = [
    path('data_throw/', views.data_throw, name="data_throw"),
    path('data_catch/', views.data_catch, name="data_catch"),
    
    path('', views.articles, name="articles"),
    path('create/', views.create, name="create"),
    path('new/', views.new_article, name="new_article"),
    path('<int:pk>/', views.article_detail, name="article_detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit', views.edit, name="edit"),
    path('<int:pk>/update', views.update, name="update"),
    
]