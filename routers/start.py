from utils.callbacks import PlanCallBack
from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(CommandStart)
async def start(message: Message, bot: Bot):
    keyboard = [
        ("😎 VIP plan", PlanCallBack(name="vip")),
        ("🎒  Master Class", PlanCallBack(name="master")),
        ("💁  One to One Mentorship", PlanCallBack(name="one_to_one")),
    ]
    buttons = InlineKeyboardBuilder()
    for text, call_back in keyboard:
        buttons.button(text=text, callback_data=call_back.pack())
    buttons.adjust(1, repeat=True)
    await bot.send_message(
        text="Welcome to our XE SNIPER Subscription Bot",
        reply_markup=buttons.as_markup(),
        chat_id=message.chat.id,
    )
