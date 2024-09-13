from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=50,unique=True)
    users_online = models.ManyToManyField(User,related_name='users_in_online',blank=True)

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
