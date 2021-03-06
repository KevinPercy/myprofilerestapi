from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myblog_api import views

router = DefaultRouter()
router.register('profiles', views.UserProfileViewSet)
router.register('posts', views.BlogPostViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
