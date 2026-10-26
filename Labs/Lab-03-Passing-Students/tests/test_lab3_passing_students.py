from grade_manager import GradeManager


def test_tc01_lower_extreme():
    manager = GradeManager()
    manager.add_student("Student1", [0])
    assert manager.get_passing_students() == []


def test_tc02_just_below_boundary():
    manager = GradeManager()
    manager.add_student("Student2", [59])
    assert manager.get_passing_students() == []


def test_tc03_boundary_value():
    manager = GradeManager()
    manager.add_student("Student3", [60])
    assert manager.get_passing_students() == ["Student3"]


def test_tc04_just_above_boundary():
    manager = GradeManager()
    manager.add_student("Student4", [61])
    assert manager.get_passing_students() == ["Student4"]


def test_tc05_upper_extreme():
    manager = GradeManager()
    manager.add_student("Student5", [100])
    assert manager.get_passing_students() == ["Student5"]


def test_tc06_multiple_grades_below_boundary():
    manager = GradeManager()
    manager.add_student("Student6", [59, 59])
    assert manager.get_passing_students() == []


def test_tc07_multiple_grades_at_boundary():
    manager = GradeManager()
    manager.add_student("Student7", [60, 60])
    assert manager.get_passing_students() == ["Student7"]


def test_tc08_multiple_grades_above_boundary():
    manager = GradeManager()
    manager.add_student("Student8", [61, 61])
    assert manager.get_passing_students() == ["Student8"]


def test_tc09_average_exactly_at_boundary():
    manager = GradeManager()
    manager.add_student("Student9", [50, 70])
    assert manager.get_passing_students() == ["Student9"]


def test_tc10_average_reaches_boundary():
    manager = GradeManager()
    manager.add_student("Student10", [59, 61])
    assert manager.get_passing_students() == ["Student10"]


def test_tc11_empty_grades():
    manager = GradeManager()
    manager.add_student("Student11", [])
    assert manager.get_passing_students() == []


def test_tc12_multiple_grades_below_boundary():
    manager = GradeManager()
    manager.add_student("Student12", [40, 50, 60])
    assert manager.get_passing_students() == []