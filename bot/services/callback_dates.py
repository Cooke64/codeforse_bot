from aiogram.filters.callback_data import CallbackData


class AlgorithmCallbackData(CallbackData, prefix='algorithm'):
    type: str


class DificultyCallbackData(CallbackData, prefix='dif'):
    type: str
