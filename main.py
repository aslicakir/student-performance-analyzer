

from sample_data import students
from student_utils import (
    calculate_average,
    get_letter_grade,
    get_pass_status,
    calculate_class_average,
)


def main():
    print("🎓 Student Performance Analyzer\n")

    for s in students:
        avg = calculate_average(s["midterm"], s["final"])
        letter = get_letter_grade(avg)
        status = get_pass_status(avg)

        print(
            f"Name: {s['name']:<8} | Midterm: {s['midterm']:>3} | Final: {s['final']:>3} "
            f"| Avg: {avg:>5.1f} | Grade: {letter} | Status: {status}"
        )

    class_avg = calculate_class_average(students)
    print("\n📌 Class Average:", f"{class_avg:.1f}")


if __name__ == "__main__":
    main()
