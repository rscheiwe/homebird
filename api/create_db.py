
import os
import json
from pysondb import db, getDb
from pysondb.db import JsonDatabase

from api.data import home_one, home_two


def where_json(file_name) -> bool:
    """

    :param str file_name: Filename for JSON DB (in .json)
    :return: True or False based on validation check
    :rtype: bool
    """
    ABS_PATH = os.path.abspath('.')
    return os.path.isfile(f"{ABS_PATH}/{file_name}") and os.access(f"{ABS_PATH}/{file_name}", os.R_OK)


def create_db() -> JsonDatabase:
    """

    :return: The PysonDB JSON database
    :rtype: JsonDatabase
    """
    if where_json('homebird.json'):
        homebird_db = getDb("homebird.json")
        return homebird_db
    else:
        homebird_db = create_db_from_scratch()
        return homebird_db


def create_db_from_scratch():
    """

    :return: The PysonDB JSON database
    :rtype: JsonDatabase
    """
    homebird_db = getDb("homebird.json")

    homebird_db.add(home_one)
    homebird_db.add(home_two)

    return homebird_db
