import asyncio
import aio_pika
import aioboto3
from coreWithClass import RouterOrchestrator

# async def process_message(message: aio_pika.IncomingMessage):
#     async with message.process():
#         print("---------queue_test----------")
#         print(message.body)
#         await asyncio.sleep(1)

# async def process_message2(message: aio_pika.IncomingMessage):
#     async with message.process():
#         print("---------queue_test2----------")
#         print(message.body)
#         await asyncio.sleep(1)        


async def main(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@localhost/", loop=loop
    )

    queue_name = "lead-delivery-started"
    other_queue = "lead-delivery-captured"
    
    print('MAIN --')

    # return await core.run_exe(connection, queue_name, other_queue)
    
    # async with connection:
    # async with connection, aioboto3.resource('dynamodb') as dynamo:
    proc = RouterOrchestrator(connection, queue_name, other_queue)
    await proc.run()

    # # Creating channel
    # channel = await connection.channel()

    # # Maximum message count which will be
    # # processing at the same time.
    # await channel.set_qos(prefetch_count=100)

    # # Declaring queue
    # queue = await channel.declare_queue(queue_name, auto_delete=True)
    # queue2 = await channel.declare_queue("test_queue2", auto_delete=True)

    # await queue.consume(process_message)
    # await queue2.consume(process_message2)

    # return connection


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    print(" [*] Waiting for messages. To exit press CTRL+C")
    loop.run_forever()