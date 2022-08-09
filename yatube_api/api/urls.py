from django.urls import include, path
from . views import GroupViewSet, PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),

]
