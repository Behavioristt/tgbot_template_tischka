import typing
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    key = 'is_private'

    def __init__(self, is_private: typing.Optional[bool] = None):
        self.is_private = is_private

    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
