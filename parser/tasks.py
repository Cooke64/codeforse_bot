from __future__ import absolute_import, unicode_literals

from celery_app import app


@app.task
def update_bd():
    from parser.main_parser import parse_codeforces
    parse_codeforces()
