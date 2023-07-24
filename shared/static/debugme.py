import csv


def get_grades() -> dict[str, list]:
    grades = {}
    with open("debug_students.csv") as f:
        for line in csv.reader(f):
            grades[line[0]] = line[1:]
    return grades


def get_avg_for(student_grades, student) -> float:
    """Return average grade for student."""
    grades = student_grades[student]
    return sum(grades)/len(grades)


def find_best_student(student_grades: dict[str, list]) -> tuple:
    """Return best student and their average grade, as a tuple."""
    best_average = -1
    best_student = None
    for student in student_grades:
        average = get_avg_for(student, student_grades[student])
        if average > best_average:
            best_average = average

    return best_student, best_average


def main():
    print("The best student is..")
    student_grades = get_grades()
    best_student, best_average = find_best_student(student_grades)
    print(f"{best_student}: best_average")


if __name__ == "__main__":
    main()