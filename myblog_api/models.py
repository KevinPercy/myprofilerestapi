from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils import timezone
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)  # takes care of the second half
        user = self.model(email=email, name=name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, last_name, password):
        """Create and save a new superuser with given details """
        user = self.create_user(email, name, last_name, password)

        user.is_superuser = True  # automatically created in the PermissionsMixin
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'last_name']

    def __str__(self):
        """Return the string representation of our user"""
        return self.email


class BlogPost(models.Model):
    """the post data"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    autor = models.CharField(max_length=35)
    is_featured = models.BooleanField(default=False)
    date_published = models.DateTimeField(default=timezone.now)
    # body = models.CharField(max_length=6000)
    body = MarkdownField(rendered_field='text_rendered',
                         validator=VALIDATOR_STANDARD)
    image_link = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    text_rendered = RenderedMarkdownField()

    def __str__(self):
        """return the post title as string"""
        return self.title
