import json
import pytest


with open("test_data/students.json", "r") as file:
    students = json.load(file)


@pytest.mark.parametrize("student", students)
def test_add_student(student, student_page):
    student_page.add_student(
        student["name"],
        student["grade"]
    )

    assert student_page.get_student_count() == 1

    added_student = student_page.get_student(0)

    assert added_student["name"] == student["name"]
    assert added_student["grade"] == str(student["grade"])