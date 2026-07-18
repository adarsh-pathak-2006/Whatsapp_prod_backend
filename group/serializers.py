from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from group.models import Group, Member, GroupChat
from contact.serializers import ProfileSerailizer
from contact.models import Profile


class GroupSerializer(ModelSerializer):
    created_by=ProfileSerailizer(read_only=True)
    class Meta:
        model=Group
        fields='__all__'


class MemberSerializer(ModelSerializer):
    group=GroupSerializer(read_only=True)
    user=ProfileSerailizer(read_only=True)
    class Meta:
        model=Member
        fields=['group', 'user', 'joined_on', 'is_admin']

class MemberUpdateSerializer(ModelSerializer):
    class Meta:
        model=Member
        fields=['is_admin']

class GroupChatSerializer(ModelSerializer):
    group=GroupSerializer(read_only=True)
    sent_by=MemberSerializer(read_only=True)
    class Meta:
        model=GroupChat
        fields='__all__'

class GroupUpdateSerializer(ModelSerializer):
    class Meta:
        model=Group
        fields=['id', 'name', 'about']