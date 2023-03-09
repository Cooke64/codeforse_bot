from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton as kb

from bot.services.callback_dates import AlgorithmCallbackData
from database.task_crud import get_all_difficulties, get_all_algorithms


def get_dificulty_kb():
    fsm_dif_kb = ReplyKeyboardBuilder()
    algorithms = get_all_difficulties()
    all_kb = [
        kb(
            text=item.type_dif[:20],
            callback_data=AlgorithmCallbackData(type=item.type_dif[:20]).pack()
        ) for item in algorithms
    ]
    fsm_dif_kb.row(*all_kb, width=3)
    return fsm_dif_kb.as_markup()


def get_alg_kb():
    fsm_dif_kb = ReplyKeyboardBuilder()
    algorithms = get_all_algorithms()
    all_kb = [
        kb(
            text=item.type[:20],
            callback_data=AlgorithmCallbackData(type=item.type[:20]).pack()
        ) for item in algorithms
    ]
    fsm_dif_kb.row(*all_kb, width=3)
    return fsm_dif_kb.as_markup()