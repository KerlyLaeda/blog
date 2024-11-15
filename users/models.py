from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.jpg", upload_to="profile_pics")
    # bio etc ?

    def __str__(self):
        return f"{self.user.username} profile"
=======

# Create your models here.
>>>>>>> a3d12e0c42f094e74ef03cbfbc1150cb0385b89a
