from django.urls import path
from chat.views import ChatAPI, ConversationAPI

urlpatterns = [
    path('', ChatAPI.as_view(), name='chat'),
    path('<int:pk>/', ConversationAPI.as_view(), name='conversation'),
]
