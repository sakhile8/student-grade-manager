"""Command-line interface for the Grade Manager."""
from grade_manager import GradeManager


def main():
    """Run a simple demo of the GradeManager."""
    manager = GradeManager()
    
    # Add your own sample students for testing
    manager.add_student("Alice", grades=[85, 90, 88])
    manager.add_student("Bob", grades=[72, 75, 78])
    manager.add_student("Charlie", grades=[95, 92, 98])
    
    print("=== Student Grade Manager Demo ===\n")
    
    # Display all students
    print("All students:")
    all_students = manager.get_all_students()
    for student in all_students:
        print(f"  - {student}")
    
    # Display passing students
    print("\nPassing students (average >= 60):")
    passing = manager.get_passing_students()
    for student in passing:
        print(f"  - {student}")
    
    try:
        print("\nAttempting to access student at index 5...")
        student = manager.students[5]  
        print(f"Student: {student['name']}")
    except IndexError as e:
        print(f"Error: {e}")
    
    print("\nDemo complete.")


if __name__ == "__main__":
    main()
