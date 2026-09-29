from grades import calculate_grade

def main():
    print("Student Result Manager v1.5 - Grade Report")
    marks = [88, 76, 95, 81, 69]

    # Input validation (resolves issue #1)
    for m in marks:
        if not isinstance(m, (int, float)) or m < 0 or m > 100:
            print(f"Invalid mark: {m}. All marks must be between 0 and 100.")
            return

    average = sum(marks) / len(marks)
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")

if __name__ == "__main__":
    main()


