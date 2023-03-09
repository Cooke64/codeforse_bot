import logging
import typing

import requests
from bs4 import BeautifulSoup as bs

from database.task_crud import add_task_in_bd


URL = 'https://codeforces.com/problemset?order=BY_RATING_ASC&locale=ru'


class UserData(typing.NamedTuple):
    number: str
    name: str
    algorithms: list[str]
    dificulty: int
    amount_done: int


def get_result(new_row: bs):
    res = []
    all_a = new_row.find_all('a')
    for i in all_a:
        new_data = i.text.strip()
        if new_data:
            res.append(new_data)
    res.append(new_row.find('span', attrs={'class': 'ProblemRating'}).text)
    return res


def make_user_data(array):
    number = array[0]
    name = array[1]
    algorithms = array[2: len(array) - 2]
    amount = int(array[-2].replace('x', ''))
    dif = int(array[-1])
    return UserData(number, name, algorithms, dif, amount)


def get_amount_of_pages() -> int:
    """Получает номер последней страницы"""
    response = requests.get(URL)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        paginator = soup.find(
            'div', attrs={'class': 'pagination'}
        ).find_all('span')[-1]
        return int(paginator.find('a').text)
    else:
        logging.error('Нет связи с сайтом.')


def push_data_in_bd(table: list[bs]):
    """Запись данных в бд"""
    for row in table[1:]:
        res = get_result(row)
        new_task = make_user_data(res)
        add_task_in_bd(
            new_task.number, new_task.name,
            new_task.dificulty, new_task.amount_done,
            new_task.algorithms
        )


def parse_current_page(num_page: int = 1) -> None:
    """
    Парсит текущую страницу с задачами. Принимает на вход номер страницы.
    """
    url = f'https://codeforces.com/problemset/page/{num_page}?order=BY_RATING_ASC&locale=ru'
    response = requests.get(url)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        table = soup.find('table', attrs={'class': 'problems'}).find_all('tr')
        push_data_in_bd(table)
    else:
        logging.error('Нет связи с сайтом.')


def parse_codeforces(pages: int = None):
    last_page = get_amount_of_pages()
    for page_number in range(1, pages if pages else last_page):
        logging.info(f'Получена страница {page_number}')
        parse_current_page(page_number)
