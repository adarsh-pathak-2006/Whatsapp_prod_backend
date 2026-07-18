from django.db import models
from contact.models import Profile


class Chat(models.Model):
    user1=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='chats')
    user2=models.ManyToManyField(Profile, related_name='chatted with')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user1.user.username

class Conversation(models.Model):
    sent_by=models.ForeignKey(Profile, on_delete=models.CASCADE)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    chat=models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.message[:80]