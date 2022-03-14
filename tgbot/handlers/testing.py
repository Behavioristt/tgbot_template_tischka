from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from tgbot.misc.test import Test


async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование\n"
                         "Вопрос 1: \n"
                         "Как тебя зовут?")


    await Test.Q1.set()


async def answer_Q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1=answer)

    await message.answer("Вопрос 2 : \n"
                         "Сколько вам лет?")
    await Test.Q2.set()


async def answer_Q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спасибо за ваши ответы!")
    await message.answer(f'Ответ 1: {answer1}')
    await message.answer(f'Ответ 2: {answer2}')

    await state.reset_state()


def register_testing(dp: Dispatcher):
    dp.register_message_handler(enter_test, Command("test"))
    dp.register_message_handler(answer_Q1, state=Test.Q1)
    dp.register_message_handler(answer_Q2, state=Test.Q2)
