from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def woman_week_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text='Dushanba'),
        KeyboardButton(text='Seshanba'),
        KeyboardButton(text='Chorshanba'),
        KeyboardButton(text='Payshanba'),
        KeyboardButton(text='Juma'),
        KeyboardButton(text='Shanba'),
            KeyboardButton(text='🔙 back')
    ])
    rkb.adjust(3,3 ,1)
    rkb = rkb.as_markup(resize_keyboard=True)
    return rkb
async def woman_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text='1-oy'),
        KeyboardButton(text='2-oy'),
        KeyboardButton(text='3-oy'),
        KeyboardButton(text='4-oy'),
        KeyboardButton(text='🔙 back')
    ])
    rkb.adjust(2,2 ,1)
    rkb = rkb.as_markup(resize_keyboard=True)
    return rkb

async def command_sart_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text='Filial 📍'),
        KeyboardButton(text='Start ✅'),
        KeyboardButton(text='Admin 👨🏻‍💻')
    ])
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    return rkb
async def sart_buttons():
    rkb = ReplyKeyboardBuilder()
    rkb.add(*[
        KeyboardButton(text='Woman 🧍‍♀️'),
        KeyboardButton(text='Men 🧍‍♂️'),
        KeyboardButton(text='🔙 back')
    ])
    rkb.adjust(2, 1)
    rkb = rkb.as_markup(resize_keyboard=True)
    return rkb
