import sys
sys.path.append("../src")
import ReadCourseData
import InsertData
import pytest

def test_from_raw_to_list_correctness():
    """
    Test if from_raw_to_list() returns the right content
    """
    course_raw = InsertData.check_file_open("test.json")
    quarter_name = 'Test Data'
    course_list, department_list = ReadCourseData.from_raw_to_list(course_raw, quarter_name)
    assert len(course_list) == 6
    assert len(department_list) == 2
    assert course_list[5].UID == department_list[1].courses[2].UID == '35528'
    assert course_list[5].crn == department_list[1].courses[2].crn == '35528'
    assert course_list[5].course_num == department_list[1].courses[2].course_num == 'D064Y'
    assert course_list[5].section_num == department_list[1].courses[2].section_num == '56'
    assert course_list[5].campus == department_list[1].courses[2].campus == 'DA'
    assert course_list[5].num_credit == department_list[1].courses[2].num_credit == 3.000
    assert course_list[5].course_title == department_list[1].courses[2].course_title == 'ADMJ INTRNSHIP'
    assert course_list[5].startTime == department_list[1].courses[2].startTime == '12:30 pm'
    assert course_list[5].endTime == department_list[1].courses[2].endTime == '03:20 pm'
    assert course_list[5].cap == department_list[1].courses[2].cap == 20
    assert course_list[5].wl_cap == department_list[1].courses[2].wl_cap == 0
    assert course_list[5].instructor_name == department_list[1].courses[2].instructor_name == 'Terry,R,Ellis'
    assert course_list[5].startDate == department_list[1].courses[2].startDate == '01/08'
    assert course_list[5].endDate == department_list[1].courses[2].endDate == '03/30'
    assert course_list[5].location == department_list[1].courses[2].location == 'DA L13C'
    assert course_list[1].location == department_list[0].courses[1].location == 'DA ONLINE'
    assert course_list[5].days == department_list[1].courses[2].days == 'MWF'
    assert course_list[1].days == department_list[0].courses[1].days == 'ONLINE'
    assert course_list[5].attribute == department_list[1].courses[2].attribute == ''

def test_from_raw_to_list_with_invalid_quarter_name():
    """
    Test if from_raw_to_list() throws the right exception if the quarter name is invalid
    """
    with pytest.raises(KeyError):
        course_raw = InsertData.check_file_open("test.json")
        quarter_name = 'Invalid quarter name'
        course_list, department_list = ReadCourseData.from_raw_to_list(course_raw, quarter_name)

def test_from_raw_to_list_with_invalid_file():
    """
    Test if from_raw_to_list() throws the right exception if the json file is invalid
    """
    with pytest.raises(FileNotFoundError):
        course_raw = InsertData.check_file_open("nonexistent.json")
        quarter_name = 'Test Data'
        course_list, department_list = ReadCourseData.from_raw_to_list(course_raw, quarter_name)
