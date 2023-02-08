
import os
from tinydb import TinyDB

from api.data import home_one, home_two, home_three


ABS_PATH = os.path.abspath('.')
FILE_NAME = 'homebird.json'


def where_json(file_name) -> bool:
    """

    :param str file_name: Filename for JSON DB (in .json)
    :return: True or False based on validation check
    :rtype: bool
    """
    return os.path.isfile(f"{ABS_PATH}/{file_name}") and os.access(f"{ABS_PATH}/{file_name}", os.R_OK)


def create_db():
    """

    :return: The PysonDB JSON database
    :rtype: JsonDatabase
    """
    if where_json(FILE_NAME):
        homebird_db = TinyDB(f"{ABS_PATH}/{FILE_NAME}")
        return homebird_db
    else:
        homebird_db = create_db_from_scratch()
        return homebird_db


def create_db_from_scratch():
    """

    :return: The PysonDB JSON database
    :rtype: JsonDatabase
    """
    homebird_db = TinyDB(f"{ABS_PATH}/{FILE_NAME}")

    homebird_db.insert(home_one)
    homebird_db.insert(home_two)
    homebird_db.insert(home_three)

    return homebird_db
