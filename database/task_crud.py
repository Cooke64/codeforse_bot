from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from bot.config import DATABASE_URI
from database.models import CodeforseTask, Algorithm, Dificulty

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()


def get_task_by_id(task_number: str) -> CodeforseTask | None:
    """
    :param task_number: Получает уникальный номер задачи
    :return: Объект CodeforseTask при его наличии
    """
    return session.query(CodeforseTask).filter(
        CodeforseTask.task_number == task_number).first()


def get_algorithm_by_id(type_algo: str) -> Algorithm | None:
    """
    :param type_algo: название алгоритма
    :return: Объект Algorithm при его наличии
    """
    return session.query(Algorithm).filter(
        Algorithm.type == type_algo).first()


def get_all_algorithms() -> list[Algorithm]:
    return session.query(Algorithm).all()


def get_all_difficulties() -> list[Dificulty]:
    return session.query(Dificulty).all()


def get_task_by_dif(dif):
    return session.query(CodeforseTask).join(Dificulty).filter(
        Dificulty.type_dif == dif).limit(10).all()


def get_dif_values(param, dif):
    return session.query(CodeforseTask).join(
        Algorithm, CodeforseTask.algorithm).filter(
        CodeforseTask.algorithm.any(
            and_(
                Algorithm.type == param,
                Dificulty.type_dif == dif,
            )
        )).all()


def create_algorithms(algorithms: list[str]) -> list[Algorithm]:
    """
    Получает список из строк в виде алгоритмов, полученных в ходе парсинга очередного ряда.
    Если такой алгоритм есть в бд, то добавляет его, если нет, создает новый.
    :return: Список объектов Algorithm.
    """
    alg_list = []
    for alg in algorithms:
        algorithm = get_algorithm_by_id(alg)
        if algorithm:
            alg_list.append(algorithm)
        else:
            alg_list.append(Algorithm(type=alg))
    return alg_list


def create_dificulty(dif: str) -> Dificulty:
    dificulty = session.query(Dificulty).filter(
        Dificulty.type_dif == dif).first()
    if not dificulty:
        new_dif = Dificulty(type_dif=dif)
        session.add(new_dif)
        session.commit()
        return new_dif
    return dificulty


def add_task_in_bd(
        task_id: str,
        name: str,
        dificulty: int,
        amount_done: int,
        algorithms: list[str]) -> None:
    if not get_task_by_id(task_id):
        new_task = CodeforseTask(
            task_number=task_id,
            name=name,
            amount_done=amount_done,
            was_in_context=None,
        )
        new_task.dificulty = create_dificulty(str(dificulty)).id
        new_task.algorithm = create_algorithms(algorithms)
        session.add(new_task)
        session.commit()


def get_tasks_list(param: str) -> list[CodeforseTask]:
    """
    Список задач по указанному алгоритму. Лимит 10 записей.
    """
    return session.query(CodeforseTask).join(
        Algorithm, CodeforseTask.algorithm).filter(
        CodeforseTask.algorithm.any(Algorithm.type == param)).limit(10).all()


def update_task_in_contest(alg_num, contest_type):
    task = get_task_by_id(alg_num)
    if not task.was_in_context:
        task.was_in_context = contest_type
        session.commit()


def get_distinc_values(param, dif):
    return session.query(CodeforseTask).join(Dificulty).filter(and_(
        CodeforseTask.was_in_context == param,
        Dificulty.type_dif == dif)).limit(10).all()
