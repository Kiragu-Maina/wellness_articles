from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/realtime/$", consumers.PromptConsumer.as_asgi()),
   
    
    
    # re_path(r"ws/managingbets/$", consumers.ManagingBetsConsumer.as_asgi()),
    
    
]