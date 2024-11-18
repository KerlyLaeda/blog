from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.jpg", upload_to="profile_pics")
    # bio etc ?

    def __str__(self):
        return f"{self.user.username} profile"

    # resize large profile pics to 300x300
    # maybe use 3p packs?
    def save(self): # args kwargs
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
