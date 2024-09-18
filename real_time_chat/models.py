from django.db import models
from django.contrib.auth.models import User
import shortuuid

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=50,unique=True,default=shortuuid.uuid)
    users_online = models.ManyToManyField(User,related_name='users_in_online',blank=True)
    groupchat_name = models.CharField(max_length=200,null=True,blank=True)
    admin = models.ForeignKey(User,null=True,blank=True,related_name="groupchats",on_delete=models.SET_NULL)
    members = models.ManyToManyField(User,related_name="chat_groups",blank=True)
    is_private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.group_name
    
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup,related_name="chat_messages",on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.Case)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.author.username} : {self.body}"
    
    class Meta:
        ordering = ["-created_at"]
