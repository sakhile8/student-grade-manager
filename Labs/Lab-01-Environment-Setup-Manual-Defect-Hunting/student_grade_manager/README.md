# Student Grade Manager - Application for Lab 1

**This is an intentionally buggy application for learning purposes.**

The goal is to read the source code carefully and identify at least **8 defects** without running any automated tools. Then, use the test suite to confirm some of your findings.

## What This App Does

The Grade Manager is a simple system for tracking students and their grades. It supports:
- Adding students to a roster
- Recording grades for each student
- Calculating average grades
- Identifying passing students (average ≥ 60)
- Generating grade reports

## Project Structure

```
student-grade-manager/
├── grade_manager.py       ← Core logic (FULL OF BUGS)
├── cli.py                 ← Command-line entry point
├── tests/
│   └── test_grades.py     ← Unit tests (some will fail)
├── pytest.ini             ← Test configuration
├── requirements.txt       ← Dependencies
└── README.md              ← This file
```

## Setup

1. **Verify Python is installed:**
   ```bash
   python --version
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python cli.py
```

This will run a demo that adds three sample students and shows their information.

## Running Tests

```bash
pytest
```

Or with verbose output:
```bash
pytest -v
```

You'll notice that some tests **fail** due to bugs in the code. This is expected!

## Lab 1 Task: Find the Defects

Your task is to:

1. **Read the code carefully** (start with `grade_manager.py`)
2. **Identify at least 8 defects** using a table:
   | ID | File | Line | Description | Severity |
   |----|------|------|-------------|----------|
   | 1  | ... | ... | ... | ... |

3. **Run the tests** and note which ones fail
4. **Reflect:** Which defects would a linter catch immediately? Which required careful thinking?

### Hints

- Look for **Python pitfalls** (e.g., mutable defaults)
- Check for **type mismatches** (e.g., string + integer)
- Watch for **logic errors** (e.g., wrong comparison operators, off-by-one loops)
- Consider **edge cases** (e.g., what happens with an empty list?)
- Verify **all code paths** (e.g., are all return statements correct?)

## Tips for Defect Hunting

1. **Read the docstrings:** They describe what each function *should* do
2. **Think about the specification:** Does the code match the expected behavior?
3. **Look for common mistakes:**
   - Loops that skip elements
   - Operations on potentially empty lists
   - Type mismatches
   - Missing return statements
   - Wrong comparison operators
4. **Use your IDE:** Hover over variables, check types, read error messages
5. **Don't run the code yet:** Resist the urge to execute. Practice manual code review.

## Reference

- [Python Documentation](https://docs.python.org/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- Common Python Pitfalls

---
