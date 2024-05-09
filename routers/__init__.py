from aiogram import Router
from .start import start_router
from .vip import vip_router
from .master_class import master_class_router
from .one_to_one import one_to_one_router
from .navigate_back import back_router
from utils.copy_router import copy_router

main_router = Router()
main_router.include_routers(
    start_router,
    vip_router,
    copy_router,
    master_class_router,
    one_to_one_router,
    back_router,
)
