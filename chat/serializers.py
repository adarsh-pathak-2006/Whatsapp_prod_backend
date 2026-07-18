from rest_framework.serializers import ModelSerializer
from chat.models import Chat, Conversation
from contact.serializers import ProfileSerailizer

class ChatSerializer(ModelSerializer):
    user1=ProfileSerailizer(read_only=True)
    user2=ProfileSerailizer(read_only=True)
    class Meta:
        model=Chat
        fields='__all__'

class Conversation(ModelSerializer):
    sent_by=ProfileSerailizer(read_only=True)
    class Meta:
        model=Conversation
        fields='__all__'