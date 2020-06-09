import sys
sys.path.append("../src")
import ReadCourseData
import InsertData
import pytest

def test_read_course_proto_correctness():
    """
    Test if read_course_proto() returns the right content with/without lab
    """
    course_raw_data = InsertData.check_file_open('test.json')
    json_obj = course_raw_data['Test Data']
    course_list = []
    department_name = 'ACCT'
    each_department = ReadCourseData.read_course_proto(json_obj, course_list, department_name)
    assert each_department.deptName == 'ACCT'
    assert len(each_department.courses) == 3
    assert each_department.courses[2].UID == course_list[2].UID == '31138'
    assert each_department.courses[2].crn == course_list[2].crn == '31138'
    assert each_department.courses[2].course_num == course_list[2].course_num == 'D105'
    assert each_department.courses[2].section_num == course_list[2].section_num == '01'
    assert each_department.courses[2].campus == course_list[2].campus == 'DA'
    assert each_department.courses[2].num_credit == course_list[2].num_credit == 1.000
    assert each_department.courses[2].course_title == course_list[2].course_title == 'BASIC FINANCIAL ACCT PROCEDURE'
    assert each_department.courses[2].startTime == course_list[2].startTime == '05:00 pm'
    assert each_department.courses[2].endTime == course_list[2].endTime == '05:50 pm'
    assert each_department.courses[2].cap == course_list[2].cap == 40
    assert each_department.courses[2].wl_cap == course_list[2].wl_cap == 5
    assert each_department.courses[2].instructor_name == course_list[2].instructor_name == 'Laurienne,Bermudez,Hammond'
    assert each_department.courses[2].startDate == course_list[2].startDate == '01/08'
    assert each_department.courses[2].endDate == course_list[2].endDate == '03/30'
    assert each_department.courses[1].location == course_list[1].location == 'DA ONLINE'
    assert each_department.courses[2].location == course_list[2].location == 'DA AT202'
    assert each_department.courses[1].days == course_list[1].days == 'ONLINE'
    assert each_department.courses[2].days == course_list[2].days == 'T'
    assert each_department.courses[2].attribute == course_list[2].attribute == ''
    assert len(each_department.courses[2].lab) == len(course_list[2].lab) == 0
    assert len(each_department.courses[1].lab) == len(course_list[1].lab) == 1
    assert each_department.courses[1].lab[0].UID == course_list[1].lab[0].UID == '35071L'
    assert each_department.courses[1].lab[0].days == course_list[1].lab[0].days == ''
    assert each_department.courses[1].lab[0].time == course_list[1].lab[0].time == 'TBA'
    assert each_department.courses[1].lab[0].startDate == course_list[1].lab[0].startDate == '06/28'
    assert each_department.courses[1].lab[0].endDate == course_list[1].lab[0].endDate == '08/07'
    assert each_department.courses[1].lab[0].instructor == course_list[1].lab[0].instructor == 'Christopher,C,Kwak'
    assert each_department.courses[1].lab[0].location == course_list[1].lab[0].location == 'DA LC107'
