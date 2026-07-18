from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_no=models.CharField(max_length=15)


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo=models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    bio=models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    contact_of=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='the_contacts')
    name=models.CharField(max_length=200, unique=True)
    contact=models.ManyToManyField(Profile, related_name='contacts', blank=True)

    def __str__(self):
        return self.name

    