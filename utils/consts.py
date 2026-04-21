#import config
import asyncio


#AUTH_URL = config.BASE_URL

#LOGIN_PAGE = f"{config.BASE_URL}/login"
def process_numbers(data):
    result = []
    for key, values in data.items():
        evens = [num for num in values if num % 2 == 0]
        if evens:
            result.append(evens)
    return result
data = {
    "a" : [1, 2, 3],
    "b" : [4, 5, 6],
    "c" : [7, 8, 9]
}
print(process_numbers(data))


def prossec_numbers_1(data):
    result = []
    for key, values in data.items():
        evens = [num for num in values if num % 2 == 0]
        if evens:
            result.extend(evens)
    return result
data = {
    "a" : [1, 2, 3],
    "b" : [4, 5, 6],
    "c" : [7, 8, 9]
}
print(prossec_numbers_1(data))


async def print1():
    print("First print")

async def print2():
    await asyncio.sleep(5)
    print("Fifth print")

async def print3():
    print("- 3")

async def print4():
    await asyncio.sleep(3)
    print("4")

async def main():
    async with asyncio.TaskGroup() as pr:
        pr.create_task(print1())
        pr.create_task(print2())
        pr.create_task(print3())
        pr.create_task(print4())

asyncio.run(main())

#asyncio.gather(print1(), print2(), print3(), print4())
#asyncio.run(mai)


