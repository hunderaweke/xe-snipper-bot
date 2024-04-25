import logging
import asyncio
from core import config
from routers import main_router
from aiogram import Bot, Dispatcher

TOKEN = config.TOKEN


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    asyncio.run(dp.start_polling(bot))
