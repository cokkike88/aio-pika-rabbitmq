import asyncio
import aio_pika
from dataclasses import dataclass

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
        queue = await channel.declare_queue(self.queue_name)
        queue2 = await channel.declare_queue(self.other_queue)

        # Exchange
        exchange = await channel.declare_exchange('kraken', aio_pika.ExchangeType.TOPIC)
        
        # Binding
        await queue.bind(exchange, 'healthcare.flow.*.started')
        await queue2.bind(exchange, 'healthcare.flow.*.captured')

        await queue.consume(self.process_message)
        await queue2.consume(self.process_message2)
    
    async def process_message(self, message: aio_pika.IncomingMessage):    
        print("********" + self.queue_name + "********")
        print(message.body)
        await asyncio.sleep(1)

    async def process_message2(self, message: aio_pika.IncomingMessage):
        print("********" + self.other_queue +"********")
        print(message.body)
        await asyncio.sleep(1)         