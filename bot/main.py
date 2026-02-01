import asyncio

async def main():
    print("Bot container is running (заглушка).")
    while True:
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
