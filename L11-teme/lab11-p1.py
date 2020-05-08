import asyncio
import random
import sys


async def suma(n):
    sum = 0
    if n == 0:
        print("n nu poate fi 0")
    else:
        for i in range(n+1):
            sum += i
        print("Suma primelor %d elemente este %d" % (n, sum))


async def main():
    q = asyncio.Queue()
    tasks = []
    for i in range(4):
        task = asyncio.create_task(suma(random.randint(0,9)))
        tasks.append(task)

    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    if sys.version_info < (3, 5):
        print("Avem nevoie de cel putin python 3.5")
        sys.exit(1)
    asyncio.run(main())
   