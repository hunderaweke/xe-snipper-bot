from aiogram.fsm.state import State, StatesGroup


class BaseStates(StatesGroup):
    MAIN_MENU = State()
    ONE_TO_ONE = State()
    VIP = State()
    MASTER_CLASS = State()
