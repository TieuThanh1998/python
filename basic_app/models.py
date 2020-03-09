from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    # Sao chép các trường trong class User sang biến user
    user = models.OneToOneField(User,on_delete=False)
    
    # addition

    portfolio_site = models.URLField(blank=True)

    # Thiết lập đường dẫn file
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
