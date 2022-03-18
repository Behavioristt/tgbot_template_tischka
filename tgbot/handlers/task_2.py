from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc.task_2 import Task2


async def answer_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    # await message.answer(str(data))
    await message.answer("Как тебя зовут?")

    await Task2.Q1.set()


async def answer_2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("Твой email?")
    await Task2.Q2.set()


async def answer_3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer2=answer)

    await message.answer("Твой номер телефона?")
    await Task2.Q3.set()


async def answer_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text

    await message.answer(  # "Спасибо за ваши ответы!\n"
                         f'Имя: {answer1}\n'
                         f'Email: {answer2}\n'
                         f'Телефон: {answer3}')

    await state.reset_state()


def register_task2(dp: Dispatcher):
    dp.register_message_handler(answer_1, Command("form"))
    dp.register_message_handler(answer_2, state=Task2.Q1)
    dp.register_message_handler(answer_3, state=Task2.Q2)
    dp.register_message_handler(answer_4, state=Task2.Q3)
