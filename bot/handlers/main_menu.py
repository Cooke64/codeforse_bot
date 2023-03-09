from aiogram import types

from bot.keyboards.inlines.alg_kb import get_algorithms_kb
from bot.keyboards.inlines.dif_kb import get_difficulty_kb


async def get_dif_tasks(message: types.Message) -> None:
    await message.answer(
        'задачи по сложности',
        reply_markup=get_difficulty_kb()
    )


async def get_algo_tasks(message: types.Message) -> None:
    await message.answer(
        'Задачи по нужным алгоритмам',
        reply_markup=get_algorithms_kb()
    )


