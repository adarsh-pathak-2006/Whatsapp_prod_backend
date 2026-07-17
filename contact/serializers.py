from rest_framework.serializers import ModelSerializer
from contact.models import User, Profile, Contact

class UserSerailizer(ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'mobile_no']

class UserDataEdit(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'mobile_no', 'password']
    
class ProfileSerailizer(ModelSerializer):
    user=UserSerailizer(read_only=True)
    class Meta:
        model=Profile
        fields=['user', 'profile_photo', 'bio']