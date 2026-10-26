
import subprocess
from pathlib import Path

repo_root = Path(__file__).resolve().parents[3]
project_folder = (
    repo_root
    / "Labs"
    / "Lab-01-Environment-Setup-Manual-Defect-Hunting"
    / "student_grade_manager"
)
source_file = project_folder / "grade_manager.py"
test_folders = [
    repo_root / "Labs" / "Lab-06-Test-Design" / "tests" / "ai_generated",
    repo_root / "Labs" / "Lab-06-Test-Design" / "tests" / "manual",
]

# Save the original source code.
original_code = source_file.read_text(encoding="utf-8")

# Each mutation changes one part of the program.
mutations = [
    {
        "name": "Passing boundary: >= 60 changed to > 60",
        "original": "if avg >= 60:",
        "mutated": "if avg > 60:",
    },
    {
        "name": "Average calculation changed",
        "original": "return total / len(grades)",
        "mutated": "return total / (len(grades) + 1)",
    },
    {
        "name": "add_grade returns False after adding a grade",
        "original": 'student["grades"].append(grade)\n                return True',
        "mutated": 'student["grades"].append(grade)\n                return False',
    },
    {
        "name": "remove_student returns False after removal",
        "original": "del self.students[i]\n                return True",
        "mutated": "del self.students[i]\n                return False",
    },
]


def run_tests():
    """Run the existing tests and return the result."""
    result = subprocess.run(
        [
            "python",
            "-m",
            "pytest",
            *(str(test_folder) for test_folder in test_folders),
            "-q",
        ],
        cwd=project_folder,
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def main():
    killed = 0
    survived = 0
    invalid = 0

    try:
        print("Checking the original program...")
        source_file.write_text(original_code, encoding="utf-8")

        if not run_tests():
            print("The original tests failed. Fix the baseline before continuing.")
            return

        print("\nOriginal tests passed. Starting mutation testing...\n")

        for mutation in mutations:
            print("=" * 60)
            print("Mutation:", mutation["name"])

            if mutation["original"] not in original_code:
                print("INVALID: The original code pattern was not found.")
                invalid += 1
                continue

            mutated_code = original_code.replace(
                mutation["original"],
                mutation["mutated"],
                1,
            )

            try:
                source_file.write_text(mutated_code, encoding="utf-8")
                tests_passed = run_tests()

                if tests_passed:
                    print("SURVIVED: The tests did not detect this change.")
                    survived += 1
                else:
                    print("KILLED: The tests detected this change.")
                    killed += 1
            finally:
                source_file.write_text(original_code, encoding="utf-8")

    finally:
        # Always restore the original program.
        source_file.write_text(original_code, encoding="utf-8")

    total = killed + survived

    print("\n" + "=" * 60)
    print("MUTATION TESTING SUMMARY")
    print("Mutations killed:", killed)
    print("Mutations survived:", survived)
    print("Invalid mutations:", invalid)

    if total:
        score = (killed / total) * 100
        print(f"Mutation score: {score:.1f}%")

    print("\nOriginal source code has been restored.")


if __name__ == "__main__":
    main()
