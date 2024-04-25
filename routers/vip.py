from .start import PlanCallBack
from utils.callbacks import ExnessCallBack, Copy
from magic_filter import F
from aiogram import Bot, Router
from aiogram.types import CallbackQuery
from aiogram.types.input_file import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_action import ChatAction

vip_router = Router()


@vip_router.callback_query(PlanCallBack.filter(F.name == "vip"))
async def vip(query: CallbackQuery, callback_data: PlanCallBack, bot: Bot):
    keyboard = [
        ("YES 👌", ExnessCallBack(status="yes")),
        ("NO  😥", ExnessCallBack(status="no")),
    ]
    buttons = InlineKeyboardBuilder()
    for text, callback in keyboard:
        buttons.button(text=text, callback_data=callback.pack())
    query.answer()

    await bot.send_message(
        chat_id=query.from_user.id,
        text="""XE VIP signa

👉🏾 LIVE TRADE 
👉🏾 daily signals  
👉🏾 XE E-BOOK 
👉🏾 more than 90% win rate  

To join xe sniper vip signal 
we require you to have an Exness account. do you have Exness account?""",
        reply_markup=buttons.as_markup(),
    )


@vip_router.callback_query(ExnessCallBack.filter(F.status == "no"))
async def no_exness(query: CallbackQuery, callback_data: ExnessCallBack, bot: Bot):
    main_text = "Create Exness Account Using this 👇 Link\n If there is any problem contact us\n**Change your Ib\!** \nAfter you finish your verification processes \nSend your screenshot and your Exness Email to this user\mn  👉🏼 Using the Button bellow"
    keyboard = [
        ("Create Exness Account", "https://one.exness-track.com/a/f5l76iz61m"),
        ("🖼️ Send Screenshot", "https://t.me/xesniper9"),
        ("💬 Contact Us", "https://t.me/xesniper9"),
        ("😎 Finish Payment", ExnessCallBack(status="pay")),
    ]
    buttons = InlineKeyboardBuilder()
    for text, var in keyboard:
        if type(var) == str and var.startswith("https"):
            buttons.button(text=text, url=var)
        else:
            buttons.button(text=text, callback_data=var)
    buttons.adjust(1, repeat=True)
    await bot.send_message(
        chat_id=query.from_user.id,
        text=main_text,
        reply_markup=buttons.as_markup(),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@vip_router.callback_query(ExnessCallBack.filter(F.status == "yes"))
async def yes_exness(query: CallbackQuery, callback_data: ExnessCallBack, bot: Bot):
    text = "**Change your Ib\!** \nAfter you finish your verification processes \nSend your screenshot and your Exness Email to us  👉🏼 Using the Button bellow and Finish Your Payment"
    keyboard = [
        ("🖼️ Send Screenshot", "https://t.me/xesniper9"),
        ("😎 Finish Payment", ExnessCallBack(status="pay")),
    ]
    video = FSInputFile("description.MP4")

    buttons = InlineKeyboardBuilder()
    for txt, var in keyboard:
        if type(var) == str and var.startswith("https"):
            buttons.button(text=txt, url=var)
        else:
            buttons.button(text=txt, callback_data=var)
    buttons.adjust(1, repeat=True)
    await bot.send_chat_action(
        chat_id=query.from_user.id, action=ChatAction.UPLOAD_VIDEO
    )
    await bot.send_video(chat_id=query.from_user.id, video=video)
    await bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=buttons.as_markup(),
        parse_mode=ParseMode.MARKDOWN_V2,
    )


@vip_router.callback_query(ExnessCallBack.filter(F.status == "pay"))
async def pay_vip(query: CallbackQuery, callback_data: ExnessCallBack, bot: Bot):
    text = "👉🏼 Using the Button bellow and Finish Your Payment and Send the screenshot to Us"
    keyboard = [
        [
            "💳 Credit Card",
            "https://buy.stripe.com/cN24gI2SA9g5bYY8ww",
        ],
        [
            "USDT(TRC20)",
            Copy(copy_type="usdt_address"),
        ],
        (
            "PayPal",
            Copy(copy_type="paypal"),
        ),
    ]
    buttons = InlineKeyboardBuilder()
    for txt, var in keyboard:
        if type(var) == str and var.startswith("https"):
            buttons.button(text=txt, url=var)
        else:
            buttons.button(text=txt, callback_data=var)
    buttons.adjust(1, repeat=True)
    await bot.send_message(
        chat_id=query.from_user.id,
        text=text,
        reply_markup=buttons.as_markup(),
        parse_mode=ParseMode.MARKDOWN_V2,
    )
