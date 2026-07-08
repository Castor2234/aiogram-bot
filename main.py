from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routes import router
import logging

load_dotenv()
TOKEN=getenv('BOT_TOKEN')

dp=Dispatcher()

dp.include_router(router)


async def main():
    logging.basicConfig(
        level=logging.WARNING,
        filename='server.log',
        filemode='a',
        format='%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    bot=Bot(token=TOKEN)

    print('Starting...')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())