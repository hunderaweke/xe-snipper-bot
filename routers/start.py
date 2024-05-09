from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from utils.callbacks import PlanCallBack

from utils.states import BaseStates

start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message, state: FSMContext, bot: Bot):
    menu_buttons = [
        [
            KeyboardButton(text="♻️ Start Over"),
            KeyboardButton(text="🛣 Show Plans"),
        ],
        [
            KeyboardButton(text="📩 Support"),
        ],
    ]
    markup = ReplyKeyboardMarkup(
        keyboard=menu_buttons,
        is_persistent=True,
        resize_keyboard=True,
    )
    await state.set_state(BaseStates.MAIN_MENU)
    await message.reply(text="Welcome", reply_markup=markup)
    await show_plans(message, bot, state)


@start_router.message(F.text == "♻️ Start Over")
@start_router.message(F.text == "🛣 Show Plans")
async def show_plans(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
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


@start_router.message(F.text == "📞 Contact")
@start_router.message(F.text == "📩 Support")
async def contact(message: Message, bot: Bot):
    await bot.send_message(
        chat_id=message.chat.id, text="Please Contact as through @Xesniper9"
    )
