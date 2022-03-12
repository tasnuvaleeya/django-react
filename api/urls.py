from django.urls import path, include
# from .views import article_list_view, article_details
# from .views import ArticleListView
# from .views import ArticleDetails
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('articles/', ArticleListView.as_view(), name='list'),
    # path('articles/<int:id>', ArticleDetails.as_view(), name='details'),
]
