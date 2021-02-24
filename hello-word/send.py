import asyncio
from aio_pika import connect, Message


async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://guest:guest@localhost/", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()

    routing_key = "typ-router-destination"
    # routing_key = "typ-router-buyer"
    # routing_key = "chiao"
    # routing_key = "hi"
    # routing_key = "test_queue"
    # routing_key = "test_queue2"

    # Sending the message
    await channel.default_exchange.publish(
        Message(b'{"session_id":100, "destinations": ["des11","des2"]}'),
        routing_key=routing_key
    )
    
    # await channel.default_exchange.publish(
    #     Message(b'{"session_id":100, "buyers": ["buyer1","buyer2"]}'),
    #     routing_key=routing_key
    # )

    print(" [x] Sent 'Hello World!'")

    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))