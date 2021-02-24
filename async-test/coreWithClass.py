import asyncio
import aio_pika
from dataclasses import dataclass

async def process_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print("---------queue_test----------")
        print(message.body)
        await asyncio.sleep(1)

async def process_message2(message: aio_pika.IncomingMessage):
    async with message.process():
        print("---------queue_test2----------")
        print(message.body)
        await asyncio.sleep(1)  


@dataclass
class RouterOrchestrator:
    rabbit: 'aio_pika.connection.Connection'
    queue_name: str
    other_queue: str

    async def run(self):
        print("Entro ----")
        channel = await self.rabbit.channel()

        # Maximum message count which will be
        # processing at the same time.
        # await channel.set_qos(prefetch_count=100)

        # Declaring queue
        queue = await channel.declare_queue(self.queue_name, auto_delete=True)
        queue2 = await channel.declare_queue(self.other_queue, auto_delete=True)

        # Exchange
        exchange = await channel.declare_exchange('kraken', aio_pika.ExchangeType.TOPIC)
        
        # Binding
        await queue.bind(exchange, 'healthcare.lead.delivery.delivered')
        await queue2.bind(exchange, 'healthcare.lead.router.routed')

        await queue.consume(self.process_message)
        await queue2.consume(self.process_message2)

        return self.rabbit
    
    async def process_message(self, message: aio_pika.IncomingMessage):    
        print("********" + self.queue_name + "********")
        print(message.body)
        await asyncio.sleep(1)

    async def process_message2(self, message: aio_pika.IncomingMessage):
        print("********" + self.other_queue +"********")
        print(message.body)
        await asyncio.sleep(1)         