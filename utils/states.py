from aiogram.fsm.state import State, StatesGroup


class BaseStates(StatesGroup):
    MAIN_MENU = State()
    ONE_TO_ONE = State()
    VIP = State()
    MASTER_CLASS = State()
    ONE_TO_ONE_COPY = State()


class VipStates(StatesGroup):
    YES = State()
    NO = State()
    PAY_YES = State()
    PAY_NO = State()
    CHOOSE_YES = State()
    CHOOSE_NO = State()
