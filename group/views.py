from django.shortcuts import get_object_or_404
from group.serializers import GroupSerializer, MemberSerializer, GroupChatSerializer, GroupUpdateSerializer, MemberUpdateSerializer
from group.models import Group, Member, GroupChat
from rest_framework.views import APIView
from contact.models import Profile
from rest_framework.response import Response


class GroupAPI(APIView):
    def get(self, request):
        profile_data=Profile.objects.get(user=request.user)
        data=Group.objects.filter(created_by=profile_data)
        serial=GroupSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=GroupSerializer(data=request.data)
        if serial.is_valid():
            profile_data=Profile.objects.get(user=request.user)
            abc=serial.save(created_by=profile_data)
            Member.objects.create(group=abc, user=profile_data, is_admin=True)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)
        
class GroupIndividualAPI(APIView):
    def get(self, request, pk):
        group_obj=get_object_or_404(Group, id=pk)
        serial=GroupSerializer(group_obj)
        return Response(serial.data, status=200)
    
    def patch(self, request, pk):
        instance=get_object_or_404(Group, id=pk)
        serial=GroupUpdateSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)
        
    def delete(self, request, pk):
        instance=get_object_or_404(Group, id=pk)
        instance.delete()
        return Response({ 'group deleted':'group successfully deleted' }, status=204)

class MemberAPI(APIView):
    def get(self, request, pk):
        group_data=get_object_or_404(Group, id=pk)
        data=Member.objects.filter(group=group_data)
        serial=MemberSerializer(data, many=True)
        return Response(serial.data, status=200)
    
    def post(self, request, pk):
        serial=MemberSerializer(data=request.data)
        if serial.is_valid():
            group_data=get_object_or_404(Group, id=pk)
            serial.save(group=group_data)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)
              
class MemberIndividualAPI(APIView):
    def get(self, request, pk, ck):
        group_data=get_object_or_404(Group, id=pk)
        data=get_object_or_404(Member, group=group_data, id=ck)
        serial=MemberSerializer(data)
        return Response(serial.data, status=200)
    
    def patch(self, request, pk, ck):
        group_data=get_object_or_404(Group, id=pk)
        instance=get_object_or_404(Member, group=group_data, id=ck)
        serial=MemberUpdateSerializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)


class GroupChatAPI(APIView):
    def get(self, request, pk):
        group_data=get_object_or_404(Group, id=pk)
        data=GroupChat(group=group_data)
        serial=GroupChatSerializer(data, many=True)
        return Response(serial.data, status=200)
    
    def post(self, request, pk):
        serial=GroupChatSerializer(data=request.data)
        if serial.is_valid():
            group_data=get_object_or_404(Group, id=pk)
            profile_data=Profile.objects.get(user=request.user)
            sent_by=Member.objects.get(user=profile_data, group=group_data)
            serial.save(sent_by=sent_by, group=group_data)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)



    
    
        


