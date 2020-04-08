from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

posts_router = DefaultRouter()
posts_router.register('posts', PostViewSet)

comments_router = DefaultRouter()
comments_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(posts_router.urls)),
    path('posts/<int:post_id>/', include(comments_router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
