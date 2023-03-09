from aiogram.fsm.state import StatesGroup, State


class ChooseAlgorithmState(StatesGroup):
    difficulty = State()
    algorithm = State()


