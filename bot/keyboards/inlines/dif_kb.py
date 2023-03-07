from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,
    InlineKeyboardButton as kb
)

from bot.services.callback_dates import DificultyCallbackData
from database.task_crud import get_all_difficulties


def get_difficulty_kb():
    dif_kb = InlineKeyboardBuilder()

    dif_types = get_all_difficulties()
    avaible_times = [
        kb(
            text=item.type_dif,
            callback_data=DificultyCallbackData(type=item.type_dif).pack()
        ) for item in dif_types]

    dif_kb.row(*avaible_times, width=3)
    return dif_kb.as_markup()
