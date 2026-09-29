from grades import calculate_grade

def main():
    print("Student Result Manager v1.0")
    marks = [85, 90, 78, 92]
    average = sum(marks) / len(marks)
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")

if __name__ == "__main__":
    main()
    