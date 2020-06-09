import sys
sys.path.append("../src")
import InsertData
import pytest

def test_check_file_open_existence_and_correctness():
	"""
    Test if check_file_open() return the correct type and
    the returned dict has the right content
    """
	result = InsertData.check_file_open("test.json")
	assert isinstance(result, dict)
	assert result

def test_check_file_open_not_exist():
	"""
    Test if check_file_open() handles correctly with a nonexistent file
    """
	with pytest.raises(FileNotFoundError):
		result = InsertData.check_file_open("nonexistent.json")
