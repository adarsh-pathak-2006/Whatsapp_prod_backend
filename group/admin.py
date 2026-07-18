from django.contrib import admin
from group.models import Group, Member, GroupChat

admin.site.register(Group)
admin.site.register(Member)
admin.site.register(GroupChat)
