import asyncio
from aio_pika import connect, IncomingMessage, ExchangeType


async def on_message(message: IncomingMessage):
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print("Message from bye channel body is: %r" % message.body)
    print("Before sleep!")
    await asyncio.sleep(5)  # Represents async I/O operations
    print("After sleep! on_message")

async def on_message2(message: IncomingMessage):
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print("OnMessage2 from bye channel body is: %r" % message.body)
    print("Before sleep!")
    await asyncio.sleep(5)  # Represents async I/O operations
    print("After sleep! on_message2")    

async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://guest:guest@localhost/", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()            

    # Declaring queue
    queue = await channel.declare_queue("hi")
    queue2 = await channel.declare_queue("chiao")
    
    # Exchange
    exchange = await channel.declare_exchange('kraken', ExchangeType.TOPIC)
    
    # Binding
    await queue.bind(exchange, 'healthcare.lead.delivery.delivered')
    await queue2.bind(exchange, 'healthcare.lead.router.routed')

    # Start listening the queue with name 'hello'
    await queue.consume(on_message, no_ack=True)
    await queue2.consume(on_message2, no_ack=True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    print(" [*] Waiting for messages. To exit press CTRL+C")
    loop.run_forever()
    