from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# NOTE: Inheriting from `User` may cause the database
#       to see duplicate users.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__():
        return self.user.username
