from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# import django_filters.rest_framework


from myblog_api import serializers
from myblog_api import models
from myblog_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class BlogPostViewSet(viewsets.ModelViewSet):
    """Handles creating and updating blog posts"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.BlogPostSerializer
    queryset = models.BlogPost.objects.all()
    permission_classes = (permissions.UpdateOwnPost, )
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend, )
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('is_featured',)

    def perform_create(self, serializer):
        """sets the user profile to the logged in user """
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned post to a given user,
        by filtering against a `is_featured` query parameter in the URL.
        """
        queryset = models.BlogPost.objects.all()
        featured = self.request.query_params.get('is_featured', None)
        if featured is not None:
            queryset = queryset.filter(is_featured=featured)
        return queryset
