import asyncio
from aio_pika import connect, Message, ExchangeType


async def main(loop):
    # Perform connection
    connection = await connect(
        "amqp://guest:guest@localhost/", loop=loop
    )

    # Creating a channel
    channel = await connection.channel()    

    routing_key = "healthcare.lead.delivery.delivered"    
    exchange_ = await channel.declare_exchange('kraken', ExchangeType.TOPIC)

    # message = b"{\"topic\":\"healthcare.lead.delivery.delivered\",\"body\":{\"sessionId\":\"20210127161059.22ss\",\"response\":[{\"destination_id\":\"boberdoo-o65\",\"output\":{\"response\":{\"status\":\"Matched\",\"lead_id\":\"58258610\",\"partners\":{\"partner\":[{\"partner_id\":\"1588\",\"company_name\":\"All Web Leads (Medicare Shared Leads - HC (16303))\",\"first_name\":\"Allison\",\"last_name\":\"Conyngham\",\"address\":\"7300 FM 2222 Bldg 2 Ste 100\",\"city\":\"Austin\",\"state\":\"TX\",\"zip\":\"78730\",\"phone\":\"5122224477\",\"email\":\"dncrequest@allwebleads.com\",\"offer\":\"<![CDATA[]]>\",\"filter_set_id\":\"44642\",\"exclusivity\":\"none\"},{\"partner_id\":\"1578\",\"company_name\":\"Health Plan One (Medicare Shared Leads - HC.com (CPA))\",\"first_name\":\"Scott\",\"last_name\":\"Conran\",\"address\":\"1000 Bridgeport Ave\",\"city\":\"Shelton\",\"state\":\"CT\",\"zip\":\"06484\",\"phone\":\"3105929926\",\"email\":\"privacy@hpone.com,sconran@hpone.com\",\"offer\":\"<![CDATA[]]>\",\"filter_set_id\":\"44402\",\"exclusivity\":\"none\"}]}}},\"status\":\"success\"}]},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1611764117}"
    # message = b"{\"topic\":\"healthcare.lead.delivery.delivered\",\"body\":{\"sessionId\":\"20210127161059.78fa38b344aa\",\"response\":[{\"destination_id\":\"boberdoo-o65\",\"output\":{\"response\":{\"status\":\"Matched\",\"lead_id\":\"58258610\",\"partners\":{\"partner\":{\"partner_id\":\"1588\",\"company_name\":\"All Web Leads (Medicare Shared Leads - HC (16303))\",\"first_name\":\"Allison\",\"last_name\":\"Conyngham\",\"address\":\"7300 FM 2222 Bldg 2 Ste 100\",\"city\":\"Austin\",\"state\":\"TX\",\"zip\":\"78730\",\"phone\":\"5122224477\",\"email\":\"dncrequest@allwebleads.com\",\"offer\":\"<![CDATA[]]>\",\"filter_set_id\":\"44642\",\"exclusivity\":\"none\"}}}},\"status\":\"success\"}]},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1611764117}"
    message = b"{\"topic\":\"healthcare.lead.delivery.delivered\",\"body\":{\"sessionId\":\"20210127161059.78fa38b6d1d83131bb\",\"response\":[{\"destination_id\":\"boberdoo-o65\",\"output\":{\"response\":{\"status\":\"Matched\",\"lead_id\":\"58258610\"}},\"status\":\"success\"}]},\"content_type\":\"\",\"exchange\":\"kraken\",\"received\":1611764117}"


# [{'destination_id': 'boberdoo-u65', 'output': {'response': {'status': 'Unmatched', 'lead_id': '13230'}}, 'status': 'success'}]
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