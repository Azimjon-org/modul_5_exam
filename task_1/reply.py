from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def email_buttons():
    rkb=ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text="Ixtiyoriy habar yuborish"))
    rkb=rkb.as_markup(resize_keyboard=True)
    return rkb
