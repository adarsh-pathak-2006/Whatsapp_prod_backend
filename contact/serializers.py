from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SlugRelatedField
from contact.models import User, Profile, Contact

class UserSerailizer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'mobile_no']


class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'mobile_no', 'password']
    
class ProfileSerailizer(ModelSerializer):
    user=UserSerailizer(read_only=True)
    class Meta:
        model=Profile
        fields=['user', 'profile_photo', 'bio']

class ContactSerailizer(ModelSerializer):
    contact=SlugRelatedField(slug_field='user__username', queryset=Profile.objects.all(), many=True)
    class Meta:
        model=Contact
        fields=['contact_of', 'name', 'contact']
        read_only_fields = ['contact_of']

class ContactUpdateSerailizer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['name']