import asyncio
import logging
import sys
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from task_2_3_4_5.bot.handlers.start_section import start_router
from task_2_3_4_5.db.models import Base, engine

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()

def before_start_checker():
    (Base.metadata.create_all(engine))
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.startup.register(before_start_checker)
    dp.include_routers(start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


