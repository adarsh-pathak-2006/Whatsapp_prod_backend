from rest_framework.serializers import ModelSerializer
from group.models import Group, Member, GroupChat
from contact.serializers import ProfileSerailizer


class GroupSerializer(ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'


class MemberSerializer(ModelSerializer):
    group=GroupSerializer(read_only=True)
    user=ProfileSerailizer(read_only=True)
    class Meta:
        model=Member
        fields=['group', 'user', 'joined_on', 'is_admin']

class GroupChatSerializer(ModelSerializer):
    group=GroupSerializer(read_only=True)
    sent_by=ProfileSerailizer(read_only=True)
    class Meta:
        model=Group
        fields='__all__'
