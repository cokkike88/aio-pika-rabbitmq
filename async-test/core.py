import asyncio
import aio_pika

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



async def run_exe(rabbit, queue_name, other_queue):
    print("Entro ----")
    channel = await rabbit.channel()

    # Maximum message count which will be
    # processing at the same time.
    #await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    queue2 = await channel.declare_queue(other_queue, auto_delete=True)

    await queue.consume(process_message)
    await queue2.consume(process_message2)

    # return rabbit