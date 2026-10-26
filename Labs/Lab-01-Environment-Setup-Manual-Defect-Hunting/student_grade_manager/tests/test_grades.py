"""Unit tests for Grade Manager."""
import pytest
from grade_manager import GradeManager


def test_add_student_returns_confirmation():
    """Test that add_student returns a confirmation value.
    
    This test will FAIL
    """
    manager = GradeManager()
    result = manager.add_student("Alice")
    assert result is not None, "add_student() should return a confirmation"


def test_get_average_empty_grades():
    """Test that get_average handles students with no grades.
    
    This test will FAIL
    """
    manager = GradeManager()
    manager.add_student("Bob", grades=[])
    average = manager.get_average("Bob")
    assert average == 0, "Average of empty grade list should be 0"


def test_get_passing_students():
    """Test that get_passing_students correctly identifies passing students.
    
    This test will FAIL 
    """
    manager = GradeManager()
    manager.add_student("Charlie", grades=[70, 80, 90])  # Average 80
    manager.add_student("Diana", grades=[40, 45, 50])     # Average 45
    
    passing = manager.get_passing_students()
    assert "Charlie" in passing, "Charlie should be in passing list (avg 80 >= 60)"
    assert "Diana" not in passing, "Diana should NOT be in passing list (avg 45 < 60)"


def test_get_all_students_includes_first():
    """Test that get_all_students includes the first student.
    
    This test will FAIL
    """
    manager = GradeManager()
    manager.add_student("Eve", grades=[88])
    manager.add_student("Frank", grades=[92])
    manager.add_student("Grace", grades=[95])
    
    all_students = manager.get_all_students()
    assert len(all_students) == 3, "Should have 3 students"
    assert "Eve" in all_students, "First student (Eve) should be in the list"
    assert all_students[0] == "Eve", "First student in list should be Eve"


def test_format_report_creates_string():
    """Test that format_report creates a valid report string.
    
    This test will FAIL
    """
    manager = GradeManager()
    manager.add_student("Henry", grades=[75, 85])
    
    report = manager.format_report("Henry")
    assert "Henry" in report, "Report should contain student name"
    assert "75" in report, "Report should contain grade 75"
    assert "85" in report, "Report should contain grade 85"


def test_add_grade_to_student():
    """Test that add_grade successfully adds a grade to a student.
    
    This test should PASS
    """
    manager = GradeManager()
    manager.add_student("Ivan", grades=[80])
    
    result = manager.add_grade("Ivan", 85)
    assert result is True, "Should successfully add grade"
    assert manager.students[0]["grades"] == [80, 85]


def test_remove_student():
    """Test that remove_student correctly removes a student.
    
    This test should PASS
    """
    manager = GradeManager()
    manager.add_student("Jack", grades=[90])
    manager.add_student("Karen", grades=[85])
    
    result = manager.remove_student("Jack")
    assert result is True, "Should successfully remove student"
    assert len(manager.students) == 1
    assert manager.students[0]["name"] == "Karen"

def test_format_report_for_nonexistent_student():
    manager = GradeManager()

    result = manager.format_report("Unknown")

    assert result == "Student 'Unknown' not found"
