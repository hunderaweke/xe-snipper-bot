from aiogram.fsm.state import State
from aiogram.filters.callback_data import CallbackData


class Copy(CallbackData, prefix="copy"):
    copy_type: str


class PlanCallBack(CallbackData, prefix="plan"):
    name: str


class ExnessCallBack(CallbackData, prefix="exness"):
    status: str


class VIPTypeCallBack(CallbackData, prefix="vip"):
    vip_type: str


class ReturnBackCallback(CallbackData, prefix="back"):
    status: str
