import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.filters.test_filter import SomeF

from tgbot.misc.throttling import rate_limit
from tgbot.models.models import User


@rate_limit(5, key="start")
async def bot_start(message: types.Message, middleware_data, from_filter, user: User):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{middleware_data=} \n{from_filter=}",
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="Простая кнопка", callback_data="button")
                                 ]
                             ]
                         ))
    logging.info(f"6. Handler")
    logging.info("Следующая точка: Post Process Message")
    return {"from_handler": "Данные из хендлера"}


async def get_button(call: types.CallbackQuery):
    await call.message.answer("Хоухоу")


# @rate_limit(limit=5, key="start")
# async def bot_start(message: types.Message, middleware_data, from_filter):
#     await message.answer(f"Привет, {message.from_user.full_name}!| \n{middleware_data=} \n{from_filter=}")
#     logging.info(f"6. Handler")
#     logging.info("Следующая точка: Post Process Message")
#     return {"from_handler": "Данные из хендлера"}


def register_bot_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart(), SomeF())
    dp.register_callback_query_handler(get_button, text="button")
