from parser.celery import app
from parser.main_parser import parse_codeforces


@app.task
def update_bd():
    parse_codeforces()
