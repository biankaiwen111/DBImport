import sys
sys.path.append("../src")
import InsertData
import ReadCourseData
import course_pb2 as course

def test_read_lab_time_correctness_lab():
    """
    Test if read_lab_time() returns the right content
    if the course has a lab
    """
    file_obj = InsertData.check_file_open("test_lab.json")
    each_course = file_obj["Test Data"]["CourseData"]["ACCT"][0]
    temp_course = course.Course()
    temp_course = ReadCourseData.read_lab_time(each_course, temp_course)
    assert len(temp_course.lab) == 1
    assert temp_course.lab[0].UID == 'L'
    assert temp_course.lab[0].days == ''
    assert temp_course.lab[0].time == 'TBA'
    assert temp_course.lab[0].startDate == '06/28'
    assert temp_course.lab[0].endDate == '08/07'
    assert temp_course.lab[0].instructor == 'Christopher,C,Kwak'
    assert temp_course.lab[0].location == 'DA LC107'

def test_read_lab_time_correctness_nolab():
    """
    Test if read_lab_time() returns the right content
    if the course has no lab
    """
    file_obj = InsertData.check_file_open("test_lab.json")
    each_course = file_obj["Test Data"]["CourseData"]["ACCT"][1]
    temp_course = course.Course()
    temp_course = ReadCourseData.read_lab_time(each_course, temp_course)
    assert len(temp_course.lab) == 0
