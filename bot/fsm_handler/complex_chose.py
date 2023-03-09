from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.handlers.tasks_callback import print_message
from bot.keyboards.replies.fsm import get_dificulty_kb, get_alg_kb
from bot.keyboards.replies.main_menu import main_menu_kb
from bot.services.states import ChooseAlgorithmState
from database.task_crud import get_dif_values, update_task_in_contest, \
    get_distinc_values


async def cmd_tasks(message: types.Message, state: FSMContext):
    await message.answer(
        'Здесь вы можете выбрать задачу по сложности и алгоритму\n Выберете сложность',
        reply_markup=get_dificulty_kb()
    )
    await state.set_state(ChooseAlgorithmState.difficulty)


async def food_chosen(message: types.Message, state: FSMContext):
    await state.update_data(difficulty=message.text)
    await message.answer(
        'Выбери алгоритм',
        reply_markup=get_alg_kb()
    )
    await state.set_state(ChooseAlgorithmState.algorithm)


async def print_result(message: types.Message, state: FSMContext):
    await state.update_data(algorithm=message.text)
    await message.answer(
        'наслаждайся задачками',
        reply_markup=main_menu_kb.as_markup()
    )
    data = await state.get_data()
    alg_type = data.get('algorithm')
    dif_type = data.get('difficulty')
    all_task = get_dif_values(alg_type, dif_type)
    for alg in all_task:
        update_task_in_contest(alg.task_number, alg_type)

    for item in get_distinc_values(alg_type, dif_type):
        mes = print_message(item)
        await message.answer(mes)
    await state.clear()