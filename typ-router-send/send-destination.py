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

    routing_key = "healthcare.lead.router.routed"
    # routing_key = "lead-router"
    # message = b"{\"topic\":\"healthcare.lead.router.routed\",\"body\":{\"sessionId\":\"20210204194600.f4aa4ff4aec2qq\",\"destinations\":[\"boberdoo-u65\",\"boberdoo-u65_+a\"],\"jornayaId\":\"047E61B2-4A64-BA1F-DAAA-0CFE42806827\",\"on\":\"2021-01-27 04:19:55.849743\"},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1611721195}"
    message = b"{\"topic\":\"healthcare.lead.router.routed\",\"body\":{\"sessionId\":\"20210127041828.3f65e7d85f92yy\",\"destinations\":[\"boberdoo-u65\"],\"jornayaId\":\"047E61B2-4A64-BA1F-DAAA-0CFE42806827\",\"on\":\"2021-01-27 04:19:55.849743\"},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1611721195}"

    # Sending the message
    await exchange_.publish(
        Message(message),
        routing_key=routing_key
    )    

    print(" [x] Sent 'Hello World!'")

    await connection.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))