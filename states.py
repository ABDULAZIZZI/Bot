from aiogram.dispatcher.filters.state import StatesGroup, State


class ContactStats(StatesGroup):
    name = State()
    age = State()
    phone = State()
