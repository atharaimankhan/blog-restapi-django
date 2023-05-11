from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from blogs.models import Blog

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    last_blog = models.ForeignKey(
        Blog,
        null=True,
        on_delete=models.SET_NULL
    )
    # add additional fields in here

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    def __str__(self) -> str:
        return self.email