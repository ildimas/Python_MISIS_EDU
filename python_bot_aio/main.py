import asyncio
import logging
import sys
from aiogram import Dispatcher
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from main_route import main_router

TOKEN = "бот токен"

default_properties = DefaultBotProperties(parse_mode="HTML")

bot = Bot(
    token=TOKEN,
    default=default_properties
)

dp = Dispatcher()

dp.include_router(main_router)

async def start_aiogram():
    await dp.start_polling(bot)
    
async def main():
    await asyncio.gather(
        start_aiogram()  
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())