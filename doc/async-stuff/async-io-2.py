import asyncio
import random


async def choose():
    return random.choice([True, False])


async def main():
    choices = await asyncio.gather(
        *[choose() for i in range(0, 100)]
    )
    print(choices)

asyncio.run(main())