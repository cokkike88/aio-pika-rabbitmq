import asyncio
import aio_pika
import aioboto3
import core
from os import environ
from coreWithClass import RouterOrchestrator

RULES_TABLE = environ.get('RULES_TABLE', 'hc-qa-typ-router-worker-destinations-dynamodb-table')

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
        "amqp://guest:guest@127.0.0.1/", loop=loop
    )

    queue_name = "test_queue"
    other_queue = "test_queue2"

    print('MAIN --')

    # return await core.run_exe(connection, queue_name, other_queue)

    async with aioboto3.resource('dynamodb') as dynamo:
        dynamo_table = await dynamo.Table(RULES_TABLE)
        proc = RouterOrchestrator(connection, queue_name, other_queue, dynamo_table)
        await proc.run(dynamo_table)

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
    connection = loop.run_until_complete(main(loop))

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())