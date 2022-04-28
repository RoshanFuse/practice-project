from channels.consumer import SyncConsumer,AsyncConsumer
from time import sleep
import asyncio

# SyncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected......',event)
        self.send({
            'type':'websocket.accept',
        })
    def websocket_receive(self, event):
        print('massage received from client',event['text'])
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            sleep(1)     
    def websocket_disconnect(self, event):
        print('disconnect.............',event)
          
  
# AsyncConsumer     
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected......',event)
        await self.send({
            'type':'websocket.accept',
        })
    async def websocket_receive(self, event):
        print('receive',event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':str(i),
            })
            await asyncio.sleep(1)
    async def websocket_disconnect(self, event):
        print('disconnect.....',event)
        
        
            