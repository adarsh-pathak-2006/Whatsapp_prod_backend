from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from contact.serializers import RegisterSerializer, UserDataEdit, ProfileSerailizer, ContactSerailizer
from contact.models import User, Profile, Contact
from rest_framework.response import Response


class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid():
            f_name=serial.validated_data['first_name']
            l_name=serial.validated_data['last_name']
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            mobile_no=serial.validated_data['mobile_no']
            password=serial.validated_data['password']

            if len(mobile_no)==10:
                if User.objects.filter(username=username).exists():
                    return Response({ 'message':'user already exists' }, status=400)
                else:
                    user_created=User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, mobile_no=mobile_no, password=password)
                    Profile.objects.create(user=user_created)
                    return Response({ 'message':'user registered successfully' }, status=201)
            else:
                return Response({ 'invalid':'invalid mobile number length' }, status=400)
        else:
            return Response(serial.errors, status=400)
        

class MyProfileAPI(APIView):
    def get(self, request):
        profile_data=get_object_or_404(Profile, user=request.user)
        serial=ProfileSerailizer(profile_data)
        return Response(serial.data, status=200)
    
    def patch(self, request):
        instance=get_object_or_404(Profile, user=request.user)
        serial=UserDataEdit(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)
        

class ContactAPI(APIView):
    def get(self, request):
        profile_data=get_object_or_404(Profile, user=request.user)
        contact_data=Contact.objects.filter(contact_of=profile_data)
        serial=ContactSerailizer(contact_data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=ContactSerailizer(data=request.data)
        if serial.is_valid():
            contact_data=get_object_or_404(Profile, user=request.user)
            serial.save(contact_of=contact_data)
            return Response({'saved':'contact saved'}, status=201)
        else:
            return Response(serial.errors, status=400)