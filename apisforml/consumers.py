# consumers.py (WebSocket consumer)
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PromptConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def prompt_user(self, event):
        prompt = event['prompt']
        await self.send(text_data=json.dumps({'prompt': prompt}))

    async def send_article(self, event):
        article_data = event['article_data']
        await self.send(text_data=json.dumps({'article': article_data}))
