from django.urls import path
from group.views import GroupAPI, GroupChatAPI, GroupIndividualAPI, MemberAPI, MemberIndividualAPI

urlpatterns = [
    path('', GroupAPI.as_view(), name='group'),
    path('<int:pk>/', GroupIndividualAPI.as_view(), name='group_individual'),
    path('member/<int:pk>/', MemberAPI.as_view(), name='member'),
    path('member/<int:pk>/<int:ck>/', MemberIndividualAPI.as_view(), name='individual_member'),
    path('chat/<int:pk>/', GroupChatAPI.as_view(), name='group_chat')
]
