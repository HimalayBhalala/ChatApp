from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name="home"),
    path('chat/<username>',get_or_create_chat, name='start-chat'),
    path('chat/room/<chatroom_name>',chat_view , name="chatroom")
]
