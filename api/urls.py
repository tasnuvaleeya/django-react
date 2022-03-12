from django.urls import path, include
from .views import article_list_view, article_details
urlpatterns = [
    path('articles/', article_list_view, name='list'),
    path('articles/<int:pk>', article_details, name='details'),
]
