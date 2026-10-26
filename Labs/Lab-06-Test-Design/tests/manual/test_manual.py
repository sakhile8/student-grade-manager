
from grade_manager import GradeManager


def test_add_grade():
    manager = GradeManager()
    manager.add_student("Alice")

    result = manager.add_grade("Alice", 85)

    assert result is True
    assert manager.students[0]["grades"] == [85]


def test_add_grade_student_not_found():
    manager = GradeManager()

    result = manager.add_grade("Alice", 85)

    assert result is False


def test_get_average():
    manager = GradeManager()
    manager.add_student("Bob", [70, 80, 90])

    result = manager.get_average("Bob")

    assert result == 80


def test_get_average_no_grades():
    manager = GradeManager()
    manager.add_student("Bob")

    result = manager.get_average("Bob")

    assert result == 0


def test_get_average_student_not_found():
    manager = GradeManager()

    result = manager.get_average("Bob")

    assert result == 0


def test_remove_student():
    manager = GradeManager()
    manager.add_student("Charlie")

    result = manager.remove_student("Charlie")

    assert result is True
    assert manager.students == []


def test_remove_student_not_found():
    manager = GradeManager()
    manager.add_student("Charlie")

    result = manager.remove_student("David")

    assert result is False
    assert manager.students == [{"name": "Charlie", "grades": []}]

