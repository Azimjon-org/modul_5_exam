import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from sqlalchemy import select, insert
from sqlalchemy.orm import Session


from task_2_3_4_5.bot.buttons.reply import command_sart_buttons
from task_2_3_4_5.bot.handlers.start_section import start_router
from task_2_3_4_5.db.models import Base, engine, User



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo("https://telegra.ph/file/d72e214d5c6e55f061970.png",
                               caption=f"""Assalomu alaykum !\n{html.bold("Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi")}"""
                         ,reply_markup=await command_sart_buttons())
    with Session(engine) as session:
        query=select(User).where(User.user_id==message.from_user.id)
        data=session.execute(query).scalar()

        user = {
            'user_id': message.from_user.id,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
        }
        if not data:
            session.execute(insert(User).values(**user))
            session.commit()

@dp.message(F.text=="Admin 👨🏻‍💻")
async def command_start_handler(message: Message) -> None:
    await message.answer("https://t.me/Absaitov_Dilshod"
                         ,reply_markup=await command_sart_buttons())



@dp.message(F.text=="Filial 📍")
async def command_start_handler(message: Message) -> None:
    await message.answer_location(latitude=41.304476,longitude=69.253043
                         ,reply_markup=await command_sart_buttons())





