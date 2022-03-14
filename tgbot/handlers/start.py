import logging

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from tgbot.filters.test_filter import SomeF
from tgbot.misc.throttling import rate_limit


@rate_limit(5, key="start")
async def bot_start(message: types.Message, middleware_data, from_filter):
    await message.answer(f"Привет, {message.from_user.full_name}! \n{middleware_data=} \n{from_filter=}")
    logging.info(f"6. Handler")
    logging.info("Следующая точка: Post Process Message")
    return {"from_handler": "Данные из хендлера"} fbd


def register_bot_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart(), SomeF())
