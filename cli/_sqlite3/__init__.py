import sqlite3
import os

from store import Store

DB_LOC = f'{os.getenv("HOME", "~")}/.dev-environment.db'
TABLE_NAME = 'environments'


class SQLiteDriver(Store):

    def __init__(self):
        self._connection = sqlite3.connect(DB_LOC)
        self._cursor = self._connection.cursor()

        self._cursor.execute(
            f'create table if not exists {TABLE_NAME}' +
            '(id integer autoincrement, name varchar, path varchar unique, image_id varchar)'
        )

    def new_environment(self, name: str, path: str, image_id: str):
        self._cursor.execute((f'insert into {TABLE_NAME} '
                              '(name, path, image_id) '
                              f'values({name}, {path}, {image_id})'))

    def find_environment(self, path_or_name: str):
        return [(entry[0], entry[1], entry[2])
                for entry in self._cursor.execute((
                    f'select name, path, image_id from {TABLE_NAME} '
                    f'where name == {path_or_name} or path == {path_or_name}'))
                ]

    def remove_environment(self):
        pass
