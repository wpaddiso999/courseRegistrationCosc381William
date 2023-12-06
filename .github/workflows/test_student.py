# tests/test_student.py
import pytest
from student import Student

def test_register_course():
    student = Student(eid="123")
    result = student.register_course("CSE", "101")
    assert result == ["CSE-101"]
