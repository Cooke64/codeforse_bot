from sqlalchemy import Column as _, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = _(
        Integer(), nullable=False,
        unique=True, primary_key=True, autoincrement=True)


class TaskAlgorithm(BaseModel):
    __tablename__ = 'task_algorithm'
    task_id = _(Integer, ForeignKey('codeforses_tasks.id'))
    algorithm_id = _(Integer, ForeignKey('algorithms.id'))


class CodeforseTask(BaseModel):
    __tablename__ = 'codeforses_tasks'

    task_number = _(String(100), unique=True, nullable=False)
    name = _(String(100), nullable=False)
    dificulty = _(Integer, ForeignKey('dificulties.id'))
    amount_done = _(Integer(), nullable=False)
    algorithm = relationship(
        'Algorithm',
        secondary='task_algorithm',
        backref='codeforses_tasks',
        overlaps='codeforses_tasks, algorithms'
    )
    was_in_context = _(String(100), nullable=True)

    def __repr__(self) -> str:
        return f"CodeforseTask(task_number={self.task_number!r}," \
               f"name={self.name!r}," \
               f" amount_done={self.amount_done!r}"


class Algorithm(BaseModel):
    __tablename__ = 'algorithms'
    type = _(String(199), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Algorithm(type={self.type!r}"


class Dificulty(BaseModel):
    __tablename__ = 'dificulties'
    type_dif = _(String(100), nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"Dificulty(type_dif={self.type_dif!r}"
