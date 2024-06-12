from aiogram.fsm.state import StatesGroup, State


class Next(StatesGroup):
    email_send=State()
    xabar_send=State()