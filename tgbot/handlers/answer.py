import re

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart, filters, Command
from aiogram.utils.deep_linking import get_start_link

from tgbot.filters.start import IsPrivate


async def bot_answer_start(message: types.Message):
    deep_link_aegs = message.get_args()
    await message.answer(f"Ты нажал на старт лошара, вот твой код {deep_link_aegs}")


async def bot_answer(message: types.Message):
    deep_link = await get_start_link(payload="123")
    await message.answer(f'привет, {message.from_user.full_name}!\n'
                         f'Ваша диплинк ссылка - {deep_link}')

    # args = message.get_args()
    # await message.answer(f"Ты передал хуйню: {args}")
    # await message.reply(message.text)


def register_answer(dp: Dispatcher):
    dp.register_message_handler(bot_answer_start, CommandStart(re.compile(r"\d\d\d")), IsPrivate(), state='*')
    dp.register_message_handler(bot_answer, CommandStart(), IsPrivate(), state='*')

