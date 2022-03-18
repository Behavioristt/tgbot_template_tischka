
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards import menu


async def show_menu(message: types.Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menu)


async def get_cotletki(message: types.Message):
    await message.answer("Вы выбрали котлетки.")


async def get_food(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())


def register_show_menu(dp: Dispatcher):
    dp.register_message_handler(show_menu, Command("menu"))
    dp.register_message_handler(get_cotletki, text="Котлетки")
    dp.register_message_handler(get_food, Text(equals=["Пюрешка", "Макарошки"]))
