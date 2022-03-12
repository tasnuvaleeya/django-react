from django.urls import path, include
# from .views import article_list_view, article_details
from .views import ArticleListView
from .views import ArticleDetails
urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='list'),
    path('articles/<int:id>', ArticleDetails.as_view(), name='details'),
]
