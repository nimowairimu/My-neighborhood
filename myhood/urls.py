from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import UserViewSet,HoodList, HoodViewset

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)
# router.register('hoods', HoodViewset)

# Users
user_signup = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_login = UserViewSet.as_view({
    'get': 'list',
    'post': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# Hoods
hoods = HoodViewset.as_view({
    'get': 'hoods',
})

view_hood = HoodViewset.as_view({
    'get': 'view_hood'
})

urlpatterns = [
    # path('api/v1',views.index),
    path('auth/signup/', user_signup, name='user_signup'),
    # path('auth/login/', user_login, name='user_login'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/view_hood/<pk>/', view_hood, name='view_hood'),
    path('api/v1/hoods/', views.HoodList.as_view()),
    path('api/v1/create_hood/', views.postHood.as_view()),
    path('api/v1/post/',views.PostList.as_view()),
    path('api/v1/allposts/',views.viewPosts.as_view()),
    path('api/v1/profile/<pk>/',views.ProfileList.as_view()),
    path('currentuser/',views.check_login,name = 'currentuser')
    # path('api/v1/', include(router.urls)),
    # path('users/<int:pk>/', user_detail, name='user-detail'),
    # path('api/v1/businesses',views.BusinessViewset)
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)