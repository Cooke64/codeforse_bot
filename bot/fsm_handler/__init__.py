__all__ = ['cmd_tasks']

from aiogram import Router, F

from bot.fsm_handler.complex_chose import cmd_tasks, food_chosen, print_result
from bot.services.states import ChooseAlgorithmState
from database.task_crud import (
    get_all_difficulties as dif,
    get_all_algorithms as alg
)


def register_fsm(router: Router):
    router.message.register(
        cmd_tasks, F.text == 'Выбрать по сложности и по алгоритму'
    )
    router.message.register(
        food_chosen,
        ChooseAlgorithmState.difficulty,
        F.text.in_([i.type_dif for i in dif()])
    )
    router.message.register(
        print_result,
        ChooseAlgorithmState.algorithm,
        F.text.in_([i.type[:20] for i in alg()])
    )
