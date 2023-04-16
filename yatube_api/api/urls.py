from django.urls import include, path
from rest_framework import routers
from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


router_v1 = routers.DefaultRouter()

router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet)
router_v1.register(
    r'follow', FollowViewSet, basename='follow'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
