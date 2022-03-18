from aiogram import Dispatcher, types
from aiogram.types import Message

from tgbot.filters.start import IsPrivate


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def admin_chat_secret(message: types.Message):
    await message.answer("Секретный текст для админов в личной переписке")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["admin"], state="*", is_admin=True)
    dp.register_message_handler(admin_chat_secret, IsPrivate(), user_id=[278660078], text="secret")
