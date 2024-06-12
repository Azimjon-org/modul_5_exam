from aiogram.fsm.state import StatesGroup, State


class Next(StatesGroup):
    choose_one=State()
    woman_month=State()
    choose_week=State()
    choose_week_back=State()