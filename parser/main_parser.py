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


def get_repsonse(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res


def get_result(new_row: bs):
    res = []
    all_a = new_row.find_all('a')
    for i in all_a:
        new_data = i.text.strip()
        if new_data:
            res.append(new_data)
    res.append(new_row.find('span', attrs={'class': 'ProblemRating'}).text)
    return res


def create_data(array):
    number = array[0]
    name = array[1]
    algorithms = array[2: len(array) - 2]
    amount = int(array[-2].replace('x', ''))
    dif = int(array[-1])
    result = UserData(number, name, algorithms, dif, amount)
    return result


def parse_codeforces():
    response = get_repsonse(URL)
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        table = soup.find('table', attrs={'class': 'problems'}).find_all('tr')
        for row in table[1:]:
            res = get_result(row)
            new_task = create_data(res)
            add_task_in_bd(
                new_task.number,
                new_task.name,
                new_task.dificulty,
                new_task.amount_done,
                new_task.algorithms
            )
    else:
        print(response.status_code)
