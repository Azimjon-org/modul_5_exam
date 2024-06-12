import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv

from task_1.email_send import email_sender
from task_1.reply import email_buttons
from task_1.state import Next

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()
useremail: str | None = None


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("Tugmani tanlang 👇!",
                         reply_markup=await email_buttons())


@dp.message(F.text == "Ixtiyoriy habar yuborish")
async def email_send(message: Message, state: FSMContext):
    await message.answer("Email kiriting : ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Next.email_send)


@dp.message(Next.email_send)
async def email_send(message: Message, state: FSMContext):
    if not message.text.endswith('@gmail.com') or not message.text[0].isalnum() or len(message.text.split('@')) != 2:
        await message.answer("""Xato email !!\nmisol:   (emailnomi@gmail.com) """)
    else:
        global useremail
        useremail = message.text
        await message.answer("""Ixtiyoriy Xabar kiriting : """)
        await state.set_state(Next.xabar_send)


@dp.message(Next.xabar_send)
async def email_send(message: Message, state: FSMContext):
    await email_sender(useremail, message.text)
    await message.answer("""Jonatildi """)
    await state.clear()



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
