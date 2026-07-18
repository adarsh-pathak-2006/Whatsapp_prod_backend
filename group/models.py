from django.db import models
from contact.models import Profile


class Group(models.Model):
    name=models.CharField(max_length=200)
    about=models.CharField(max_length=500, blank=True, null=True)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE, name='member_in_the_group')
    user=models.ManyToManyField(Profile, related_name='groups')
    joined_on=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.group.name
    
class GroupChat(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    sent_by=models.ForeignKey("group.Member", on_delete= models.CASCADE)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:80]
