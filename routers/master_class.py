from aiogram import Router
from utils.callbacks import Copy, PlanCallBack
from magic_filter import F
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.states import BaseStates
from utils.callbacks import ReturnBackCallback

master_class_router = Router()


@master_class_router.callback_query(PlanCallBack.filter(F.name == "master"))
async def master_class(
    query: CallbackQuery, callback_data: PlanCallBack, bot: Bot, state: FSMContext
):
    text = """XE Sniper Master Class Program

✅Basic to advanced forex trading knowledge
✅Advanced Trading Psychology
✅Risk and money management
✅Access our Discord community
✅Access a free-quality gold signal for one month
✅24/7 student guidance
✅A big giveaway at the end of the class
✅Course duration: 3 month
💸Payment: 100$ or 10000
Finish Your Payment Using One of the methods and send the screenshot to @xesniper9"""
    keyboard = [
        (
            "💳 Credit Card",
            "https://buy.stripe.com/dR66oQ1Ow2RH3ssaEF",
        ),
        (
            "🪙 USDT(TRC20)",
            Copy(copy_type="usdt_address"),
        ),
        (
            "🏦 CBE(Bank)",
            Copy(copy_type="bank_account"),
        ),
        (
            "✅ PayPal",
            Copy(copy_type="paypal"),
        ),
        (
            "🔙 Back",
            ReturnBackCallback(status="back"),
        ),
    ]
    buttons = InlineKeyboardBuilder()
    for txt, var in keyboard:
        if type(var) == str and var.startswith("https"):
            buttons.button(text=txt, url=var)
        else:
            buttons.button(text=txt, callback_data=var)
    await state.clear()
    await state.set_state(BaseStates.MASTER_CLASS)
    await bot.delete_message(
        chat_id=query.from_user.id, message_id=query.message.message_id
    )
    buttons.adjust(1, repeat=True)
    await bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=buttons.as_markup(),
    )
