__all__ = ['get_algo_tasks', 'get_dif_tasks']

from aiogram import Router, F

from bot.commands import start_command
from bot.handlers.main_menu import get_dif_tasks, get_algo_tasks
from bot.handlers.tasks_callback import get_tasks, get_tasks_by_dif
from bot.services.callback_dates import (
    AlgorithmCallbackData,
    DificultyCallbackData
)


def register_main_menu(router: Router):
    router.message.register(start_command, F.text == 'Главная')
    router.message.register(get_algo_tasks, F.text == 'По категориям')
    router.message.register(get_dif_tasks, F.text == 'По сложности')
    # router.callback_query.register(
    #     get_tasks,
    #     AlgorithmCallbackData.filter()
    # )
    # router.callback_query.register(
    #     get_tasks_by_dif,
    #     DificultyCallbackData.filter()
    # )

