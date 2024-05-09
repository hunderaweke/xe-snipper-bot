from aiogram import Router
from core import config
from utils import copy_router
from .callbacks import Copy
from magic_filter import F
from aiogram import Bot
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext

from .callbacks import ReturnBackCallback

copy_router = Router()


@copy_router.callback_query(Copy.filter(F.copy_type == "usdt_address"))
async def copy_usdt_address(
    query: CallbackQuery, callback_data: Copy, bot: Bot, state: FSMContext
):
    keyboard = [
        (
            "🖼️ Send Screenshot",
            "https://t.me/xesniper9",
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
    await bot.delete_message(
        chat_id=query.from_user.id, message_id=query.message.message_id
    )
    await bot.send_message(
        chat_id=query.from_user.id,
        text=f"Copy the Address below: 👇\n\n` {config.USDT_ADDRESS} ` \n\nFinish the payment and send screen shot to @xesniper9",
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=buttons.as_markup(),
    )


@copy_router.callback_query(Copy.filter(F.copy_type == "bank_account"))
async def copy_bank_account(
    query: CallbackQuery, callback_data: Copy, bot: Bot, state: FSMContext
):
    await state.set_state(callback_data.state)
    await bot.delete_message(
        chat_id=query.from_user.id, message_id=query.message.message_id
    )

    await bot.send_message(
        chat_id=query.from_user.id,
        text="TEYIBA MOHAMMED \n`1000540470573`",
        parse_mode=ParseMode.MARKDOWN,
    )


@copy_router.callback_query(Copy.filter(F.copy_type == "paypal"))
async def paypal_copy(
    query: CallbackQuery, callback_data: Copy, bot: Bot, state: FSMContext
):
    await bot.delete_message(
        chat_id=query.from_user.id, message_id=query.message.message_id
    )
    await state.set_state(callback_data.state)

    await bot.send_message(
        chat_id=query.from_user.id,
        text="👇 Here is the Paypal Email 📬:\n\n`salsyitayew@gmail.com`\n\nFinish the payment and send screenshot to @xesniper9",
        parse_mode=ParseMode.MARKDOWN,
    )
