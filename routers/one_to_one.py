from aiogram import Router
from utils.callbacks import Copy, PlanCallBack
from magic_filter import F
from aiogram import Bot
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

one_to_one_router = Router()


@one_to_one_router.callback_query(PlanCallBack.filter(F.name == "one_to_one"))
async def one_to_one(query: CallbackQuery, callback_data: PlanCallBack, bot: Bot):
    keyboard = [
        (
            "💳 Credit Card",
            "https://buy.stripe.com/7sI9B264Mdwl4ww146",
        ),
        (
            "USDT(TRC20)",
            Copy(copy_type="usdt_address"),
        ),
        (
            " PayPal",
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
        text="""XE Sniper One to One Mentorship Program

✅Basic to advanced forex trading knowledge
✅Advanced Trading Psychology
✅Risk and money management
✅Access our Discord community.
✅Access a free-quality gold signal for one month
✅24/7 student guidance
✅A big giveaway at the end of the class
✅Get Xe Sniper Digital Certificate
✅Course duration: 1 month and 15 days
💸Payment: 500$\n
Finish Your Payment Using One of the methods and send the screenshot to @xesniper9""",
        reply_markup=buttons.as_markup(),
    )
