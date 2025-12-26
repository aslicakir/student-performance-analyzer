

def calculate_average(midterm: float, final: float) -> float:
    """Calculates weighted average: midterm 40%, final 60%."""
    return midterm * 0.40 + final * 0.60


def get_letter_grade(average: float) -> str:
    """Returns letter grade based on average."""
    if average >= 85:
        return "AA"
    elif 70 <= average <= 84:
        return "BB"
    elif 60 <= average <= 69:
        return "CC"
    else:
        return "FF"


def get_pass_status(average: float) -> str:
    """Returns 'Passed' if average >= 60 else 'Failed'."""
    return "Passed" if average >= 60 else "Failed"


def calculate_class_average(students: list) -> float:
    """
    Takes a list of student dicts and returns overall class average.
    Expected keys: 'midterm', 'final'
    """
    if not students:
        return 0.0

    total = 0.0
    for s in students:
        total += calculate_average(s["midterm"], s["final"])

    return total / len(students)
