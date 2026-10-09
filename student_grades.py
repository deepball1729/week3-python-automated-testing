"""Student grade utilities for Week 3 automated testing."""

def calculate_average(scores):
    """Return average of scores between 0 and 100."""
    scores = list(scores)
    if not scores:
        raise ValueError("At least one score is required.")
    values = []
    for score in scores:
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("All scores must be numeric values.")
        if not 0 <= score <= 100:
            raise ValueError("Scores must be between 0 and 100.")
        values.append(float(score))
    return sum(values) / len(values)


def get_grade(score):
    """Convert a score from 0 to 100 into a letter grade."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"


def build_report(student_scores):
    """Create grades and summary statistics from {student_name: score}."""
    if not isinstance(student_scores, dict):
        raise TypeError("student_scores must be a dictionary.")
    if not student_scores:
        raise ValueError("At least one student is required.")
    grades, values = {}, []
    for name, score in student_scores.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student names must be non-empty strings.")
        clean_name = name.strip()
        grades[clean_name] = get_grade(score)
        values.append(float(score))
    return {
        "grades": grades,
        "class_average": sum(values) / len(values),
        "highest_score": max(values),
        "lowest_score": min(values),
        "student_count": len(values),
    }
