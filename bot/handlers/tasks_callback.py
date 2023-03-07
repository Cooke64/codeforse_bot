from aiogram import types

from bot.keyboards.inlines.alg_kb import get_algorithms_kb
from bot.keyboards.inlines.dif_kb import get_difficulty_kb
from bot.services.callback_dates import AlgorithmCallbackData
from database.models import CodeforseTask, Dificulty
from database.task_crud import get_tasks_list, get_task_by_dif, session


def print_message(instanse: CodeforseTask) -> str:
    reply_message = f"""
Задача {instanse.task_number} {instanse.name} со сложностью {session.query(Dificulty).get(instanse.dificulty).type_dif}.
Решена {instanse.amount_done} раз \n
рекомендуемые алгоритмы для решения {', '.join([item.type for item in instanse.algorithm])}\n
"""
    return reply_message


async def get_tasks(call: types.CallbackQuery,
                    callback_data: AlgorithmCallbackData) -> None:
    data = get_tasks_list(callback_data.type)
    for item in data:
        mes = print_message(item)
        await call.message.answer(mes)

    await call.message.answer(
        'задачи по категориям алгоритмов',
        reply_markup=get_algorithms_kb()
    )


async def get_tasks_by_dif(
        call: types.CallbackQuery,
        callback_data: AlgorithmCallbackData) -> None:
    data = get_task_by_dif(callback_data.type)
    for item in data:
        mes = print_message(item)
        await call.message.answer(mes)
    await call.message.answer(
        'задачи по сложности',
        reply_markup=get_difficulty_kb()
    )
