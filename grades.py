def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

def calculate_percentage(marks, max_marks=100):
    return (sum(marks) / (len(marks) * max_marks)) * 100