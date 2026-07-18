from django.shortcuts import render, get_object_or_404
from chat.serializers import ChatSerializer, ConversationSerializer
from chat.models import Chat, Conversation
from rest_framework.generics import ListCreateAPIView
from contact.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from whatsapp.throttle import BasicThrottle
from django.db.models import Q


class ChatAPI(ListCreateAPIView):
    throttle_classes=[BasicThrottle]
    permission_classes=[IsAuthenticated]
    serializer_class=ChatSerializer

    def get_queryset(self):
        user_data=Profile.objects.get(user=self.request.user)
        return Chat.objects.filter(Q(user1=user_data) | Q(user2=user_data)).distinct()

    def perform_create(self, serializer):
        user_data=Profile.objects.get(user=self.request.user)
        chat = serializer.save(user1=user_data)
        
        user2_username = self.request.data.get('user2')
        if user2_username:
            from contact.models import User
            try:
                target_user = User.objects.get(username=user2_username)
                target_profile = Profile.objects.get(user=target_user)
                chat.user2.add(target_profile)
            except Exception:
                pass

class ConversationAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        user_data=get_object_or_404(Profile, user=request.user)
        chat_data=get_object_or_404(Chat, id=pk)
        if chat_data.user1 != user_data and not chat_data.user2.filter(id=user_data.id).exists():
            return Response({"error": "Forbidden"}, status=403)
        convo=Conversation.objects.filter(chat=chat_data)
        serial=ConversationSerializer(convo, many=True)
        return Response(serial.data, status=200)
    
    def post(self, request, pk):
        serial=ConversationSerializer(data=request.data)
        if serial.is_valid():
            user_data=get_object_or_404(Profile, user=request.user)
            chat_data=get_object_or_404(Chat, id=pk)
            if chat_data.user1 != user_data and not chat_data.user2.filter(id=user_data.id).exists():
                return Response({"error": "Forbidden"}, status=403)
            serial.save(chat=chat_data, sent_by=user_data)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)
    
