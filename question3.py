# Using loop of your choice,WITI has tasked you to automate a simple
# program using functions and conditions to display the grades that
# the students will be receiving.
# The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# < 50%     Fail
# Solution
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'Fail'

def main():
    num_students = int(input("Enter the number of students: "))
    grades = {}

    for i in range(num_students):
        score = float(input(f"Enter score for student {i + 1}: "))
        grade = determine_grade(score)
        grades[f'Student {i + 1}'] = grade

    print("\nGrades:")
    for student, grade in grades.items():
        print(f"{student}: {grade}")

if __name__ == "__main__":
    main()
