import sys
sys.path.append("../src")
import InsertData
import pymongo
import pytest

def test_get_db_existence():
    """
    Test if get_db() return the correct type
    """
    db = InsertData.get_db()
    assert isinstance(db, pymongo.database.Database)
