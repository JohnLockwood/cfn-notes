import asyncio
import time


async def wait_print(item, delay):
    t = time.strftime("Starting at %H:%M:%S", time.localtime())
    print(f'Start {item} at time {t}')
    await asyncio.sleep(delay)
    t = time.strftime("Starting at %H:%M:%S", time.localtime())
    print(f'End {item} at time {t}')


async def main():
    print("Hello")
    print(time.strftime("Starting at %H:%M:%S", time.localtime()))
    coroutine = wait_print("A", 2)
    print(str(type(coroutine)))
    await coroutine
    await wait_print("B", 2)
    print(time.strftime("Two consecutive finished at %H:%M:%S", time.localtime()))
    t1 = asyncio.create_task(wait_print("C", 2))
    t2 = asyncio.create_task(wait_print("D", 2))
    t3 = asyncio.create_task(wait_print("E", 2))

    await t1
    await t2
    try:
        t3.cancel()
    except asyncio.CancelledError:
        print("t3 cancelled!")

    print(time.strftime("Two simultaneous finished at %H:%M:%S", time.localtime()))

asyncio.run(main())