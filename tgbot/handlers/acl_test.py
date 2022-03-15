from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from tgbot.models.models import User


async def block_me(message: types.Message, user: User):
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ запрещен. /n"
                         f"Разблокировать можно по команде /unblock_me")
    user.block()


async def unblock_me(message: types.Message, user: User):
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен. /n"
                         f"Разблокировать можно по команде /unblock_me")
    user.allow()


def register_acl_test(dp: Dispatcher):
    dp.register_message_handler(block_me, CommandStart("block_me"))
    dp.register_message_handler(unblock_me, CommandStart("unblock_me"))
