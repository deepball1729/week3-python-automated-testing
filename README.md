# Week 3: Automated Testing for Python Applications

This project demonstrates automated tests for a student-grade utility module using Python's built-in `unittest` framework. No third-party packages or external datasets are needed.

## Files
- `student_grades.py`: average, grade conversion, and class report functions.
- `test_student_grades.py`: automated unit and component-integration tests.
- `debugging_report.docx`: Word report describing test cases and methodology.
- `test_results.txt`: output from running the test suite in the creation environment.

## Run tests
Open a terminal in this folder and run:

```bash
python -m unittest -v
```

## Example
```python
from student_grades import build_report
print(build_report({"Asha": 95, "Ravi": 75, "Meera": 85}))
```

Tests cover normal values, grade boundaries, empty inputs, invalid types, out-of-range scores, blank names, and summary calculations. For strict TDD, write a test first, run it to observe failure, implement the smallest fix, and rerun the suite. Describe only the workflow you actually followed in your submission.
