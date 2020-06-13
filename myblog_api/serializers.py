from rest_framework import serializers
from myblog_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "last_name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"]
        )

        return user


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer of blob post model"""
    class Meta:
        model = models.BlogPost
        fields = ("id", "user_profile", "title",
                  "autor", "is_featured", "date_published", "body",
                  "image_link", "description", "text_rendered")
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
