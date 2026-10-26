import pytest
from grade_manager import GradeManager


def test_add_grade_successfully_adds_grade():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.add_grade("Alice", 85)

    assert result is True
    assert manager.students[0]["grades"] == [85]


def test_add_grade_to_existing_grades():
    manager = GradeManager()
    manager.add_student("Alice", [70, 80])

    result = manager.add_grade("Alice", 90)

    assert result is True
    assert manager.students[0]["grades"] == [70, 80, 90]


def test_add_grade_returns_false_for_nonexistent_student():
    manager = GradeManager()

    result = manager.add_grade("Alice", 85)

    assert result is False
    assert manager.students == []


def test_get_average_returns_average_of_grades():
    manager = GradeManager()
    manager.add_student("Alice", [70, 80, 90])

    result = manager.get_average("Alice")

    assert result == 80


def test_get_average_returns_zero_for_student_with_no_grades():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.get_average("Alice")

    assert result == 0


def test_get_average_returns_zero_for_nonexistent_student():
    manager = GradeManager()

    result = manager.get_average("Alice")

    assert result == 0


def test_remove_student_successfully_removes_student():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.remove_student("Alice")

    assert result is True
    assert manager.students == []


def test_remove_student_returns_false_for_nonexistent_student():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.remove_student("Bob")

    assert result is False
    assert manager.students == [{"name": "Alice", "grades": []}]


def test_remove_student_only_removes_matching_student():
    manager = GradeManager()
    manager.add_student("Alice")
    manager.add_student("Bob")

    result = manager.remove_student("Alice")

    assert result is True
    assert manager.students == [{"name": "Bob", "grades": []}]


def test_add_grade_does_not_match_a_different_existing_student():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.add_grade("Bob", 85)

    assert result is False
    assert manager.students == [{"name": "Alice", "grades": []}]


def test_get_average_preserves_fractional_averages():
    manager = GradeManager()
    manager.add_student("Alice", [70, 71])

    assert manager.get_average("Alice") == 70.5


def test_get_passing_students_includes_exactly_sixty():
    manager = GradeManager()
    manager.add_student("Alice", [60])
    manager.add_student("Bob", [59])

    assert manager.get_passing_students() == ["Alice"]
