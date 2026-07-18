from django.shortcuts import render, get_object_or_404
from chat.serializers import ChatSerializer, ConversationSerializer
from chat.models import Chat, Conversation
from rest_framework.generics import ListCreateAPIView
from contact.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from whatsapp.throttle import BasicThrottle


class ChatAPI(ListCreateAPIView):
    throttle_classes=[BasicThrottle]
    permission_classes=[IsAuthenticated]
    serializer_class=ChatSerializer

    def get_queryset(self):
        user_data=Profile.objects.get(user=self.request.user)
        return Chat.objects.filter(user1=user_data)

class ConversationAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        user_data=get_object_or_404(Profile, user=request.user)
        chat_data=get_object_or_404(Chat, user1=user_data, id=pk)
        convo=Conversation.objects.filter(chat=chat_data, sent_by=user_data)
        serial=ConversationSerializer(convo, many=True)
        return Response(serial.data, status=200)
    
    def post(self, request, pk):
        serial=ConversationSerializer(data=request.data)
        if serial.is_valid():
            user_data=get_object_or_404(Profile, user=request.user)
            chat_data=get_object_or_404(Chat, user1=user_data, id=pk)
            serial.save(chat=chat_data, sent_by=user_data)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)
    
