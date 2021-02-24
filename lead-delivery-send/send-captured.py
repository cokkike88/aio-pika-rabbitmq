import asyncio
from aio_pika import connect, Message, ExchangeType


async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://guest:guest@localhost/", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()
    exchange_ = await channel.declare_exchange('kraken', ExchangeType.TOPIC)

    routing_key = "healthcare.flow.*.captured"   

    await exchange_.publish(
        Message(b"{\"topic\":\"healthcare.flow.*.captured\",\"body\":{\"sessionId\":\"20210204194600.f4aa4ff4aec2tw\",\"score\":0.888,\"jornayaId\":\"08715BA3-7FC3-0113-1CA8-988BD83DD51D\",\"on\":\"2021-02-01 18:09:05.477247\"},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1612202945}"),
        routing_key=routing_key
    )

    print(" [x] Sent ")

    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))