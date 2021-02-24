from subprocess import check_output
import asyncio


def print_contents_of_cwd():
    return check_output(['ls']).split()


async def get_data():
    await asyncio.sleep(3)
    data = {
        "name": "liss",
        "age": "30"
    }
    return data


async def get_data_to_print():
    result = await get_data()
    print(result);
    return result["body"]