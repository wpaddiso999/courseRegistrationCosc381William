# tests/test_student.py
import pytest
from student import Student

## Move all the files out of the .github/workflows (except for the blank.yml)
## Follow the GitHub flow (creating an issue, create a branch, commits, and do pull request)
## You need to add the following items in "test_student.py":
##   * fixture to create a Student in this file, and use the fixture in the test
##   * mocker to mock the method "is_valid_course" in a new test

def test_register_course():
    student = Student(eid="123")
    result = student.register_course("CSE", "101")
    assert result == ["CSE-101"]
