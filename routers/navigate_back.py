from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from .start import show_plans
from .one_to_one import one_to_one
from .vip import *
from utils.states import BaseStates, VipStates
from utils.callbacks import ReturnBackCallback

back_router = Router()


@back_router.callback_query(ReturnBackCallback.filter(F.status == "back"))
async def back(
    query: CallbackQuery, state: FSMContext, bot: Bot, callback_data: ReturnBackCallback
):
    curr_state = await state.get_state()
    if curr_state in {BaseStates.ONE_TO_ONE, BaseStates.VIP, BaseStates.MASTER_CLASS}:
        await show_plans(query.message, bot, state)
    elif curr_state == BaseStates.ONE_TO_ONE_COPY:
        await one_to_one(query, callback_data, bot, state)
    elif curr_state == VipStates.CHOOSE_NO:
        await no_exness(query, callback_data, bot, state)
    elif curr_state == VipStates.CHOOSE_YES:
        await yes_exness(query, callback_data, bot, state)
    elif curr_state == VipStates.PAY_YES:
        await vip(query, callback_data, bot, state)
    elif curr_state == VipStates.PAY_NO:
        await vip(query, callback_data, bot, state)
