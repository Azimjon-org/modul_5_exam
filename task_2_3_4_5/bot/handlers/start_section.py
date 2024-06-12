from aiogram import Router, F,html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from task_2_3_4_5.bot.buttons.reply import sart_buttons, command_sart_buttons, woman_buttons, woman_week_buttons
from task_2_3_4_5.bot.state.states import Next

start_router = Router()


@start_router.message(F.text=="Start ✅")
async def start_handler(message: Message,state :FSMContext) -> None:
    await message.answer("Quydagilardan birontasini tanlang 👇🏿"
                         ,reply_markup=await sart_buttons())
    await state.set_state(Next.choose_one)

@start_router.message(Next.choose_one)
async def choose_one_handler(message: Message,state :FSMContext) -> None:
    if message.text=="Woman 🧍‍♀️":
        await message.answer_photo("https://telegra.ph/file/d84f9e8df5ba5446e05c1.png",
                                   caption=f"""Quydagilarni birontasini tanlang 👇🏿"""
                                   , reply_markup=await woman_buttons())
        await state.set_state(Next.woman_month)

    elif message.text=="Men 🧍‍♂️️":
        pass
    else:
       await state.clear()
       await message.answer_photo("https://telegra.ph/file/d72e214d5c6e55f061970.png",
                                  caption=f"""Assalomu alaykum !\n{html.bold("Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi")}"""
                                  , reply_markup=await command_sart_buttons())



@start_router.message(Next.woman_month)
async def woman_month_handler(message: Message,state :FSMContext) -> None:
    if message.text=='🔙 back':
        await message.answer("Quydagilardan birontasini tanlang 👇🏿"
                             , reply_markup=await sart_buttons())
        await state.set_state(Next.choose_one)
    else :
        await message.answer("Hafta kunlaridan birontasini tanlang",
                             reply_markup=await woman_week_buttons() )
        await state.set_state(Next.choose_week)



@start_router.message(Next.choose_week)
async def woman_choose_week_handler(message: Message,state :FSMContext) -> None:
    if message.text=="🔙 back":
        await message.answer("Quydagilardan birontasini tanlang 👇🏿"
                             , reply_markup=await sart_buttons())
        await state.set_state(Next.choose_one)



