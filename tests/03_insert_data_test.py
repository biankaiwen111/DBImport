import sys
sys.path.append("../src")
from configparser import ConfigParser
from pathlib import Path
import InsertData
import ReadCourseData

env_config = ConfigParser()
env_config.read(Path('..') / 'config' / 'setting.config')
mongo_config = env_config['MongoDB']

def test_insert_data_correctness():
    """
    Test if insert_data() returns the right content
    """
    course_raw_data = InsertData.check_file_open('test.json')
    course_list, department_list = ReadCourseData.from_raw_to_list(course_raw_data, 'Test Data')
    InsertData.insert_data(course_list, department_list, 'Test Data')
    db = InsertData.get_db()
    assert (db['Test Data courses'].find_one({'crn': '32072'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '35071'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '31138'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '00053'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '00054'})) is not None
    assert (db['Test Data courses'].find_one({'crn': '35528'})) is not None
    assert (db['Test Data departments'].find_one({'deptName': 'ACCT'})) is not None
    assert (db['Test Data departments'].find_one({'deptName': 'ADMJ'})) is not None
    assert len(db['Test Data departments'].find_one({'deptName': 'ACCT'})['courses']) == 3
    assert len(db['Test Data departments'].find_one({'deptName': 'ADMJ'})['courses']) == 3
    

