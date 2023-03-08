from aiogram.utils.keyboard import InlineKeyboardBuilder, \
    InlineKeyboardButton as kb

from bot.services.callback_dates import AlgorithmCallbackData
from database.task_crud import get_all_algorithms


def get_algorithms_kb():
    algorithms = get_all_algorithms()
    new_kb = InlineKeyboardBuilder()
    all_kb = [
        kb(
            text=item.type,
            callback_data=AlgorithmCallbackData(type=str(item.type)).pack()
        ) for item in algorithms
    ]
    new_kb.row(*all_kb, width=3)
    return new_kb.as_markup()
