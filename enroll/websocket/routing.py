from django.urls import path
from enroll.websocket import consumers

# for websocketing urls
websocket_urlpatterns = {
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi())
}