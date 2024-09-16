from django.contrib import admin
from .models import ChatGroup,GroupMessage

# Register your models here.

class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ["id","group_name","is_private"]
admin.site.register(ChatGroup,ChatGroupAdmin)

class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ["id","group","author","body","created_at"]
admin.site.register(GroupMessage,GroupMessageAdmin)
