from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import *
from .forms import *

@login_required
def chat_view(request,chatroom_name="Public-Chat"):    
    chat_group = get_object_or_404(ChatGroup,group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()

        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break

    form = ChatmessageCreateForm()

    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()

            context = {
                "message":message,
                "user":request.user
            }

            return render(request,'real_time_chat/partials/chat_message_p.html',context)

    context = {
        "chat_messages":chat_messages,
        "form":form,
        "other_user":other_user,
        "chatroom_name":chatroom_name
    }

    return render(request, 'real_time_chat/chat.html',context)


def get_or_create_chat(request,username):
    
    if request.user.username == username:
        return redirect('home')

    other_user = User.objects.get(username=username)
    mychatrooms = request.user.chat_groups.filter(is_private=True)
    if mychatrooms.exists():
        for chatroom in mychatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(is_private=True)
                chatroom.members.add(other_user,request.user)
    else:
        chatroom = ChatGroup.objects.create(is_private=True)
        chatroom.members.add(other_user,request.user)

    return redirect("chatroom",chatroom.group_name)

def create_new_group_chat(request):
    return render(request,'real_time_chat/create_groupchat.html')