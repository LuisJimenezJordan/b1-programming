student_records = {}

print("Welcome to Student Grade Analyzer")

while True:
    print("\nGrade Analyzer Menu:")
    print("1. Enter Grades for One Student")
    print("2. Enter Grades for Multiple Students")
    print("3. View Individual Student Data")
    print("4. View Class Statistics")
    print("5. Exit")

    ans = input("Enter your choice: ")

    if ans == '1':
        print("Enter Student Data:")
        name = input(" Student Name: ")
        score = int(input(" Score: "))
        student_records[name] = score

    elif ans == '2':
        print("Enter Student data for entire class (6 students)")
        for i in range(1, 7):
            print(f"Enter Student Information #{i}:")
            name = input(" Student Name: ")
            score = int(input(" Score: "))
            student_records[name] = score

    elif ans == '3':
        print('===SEARCH INDIVIDUAL STUDENT DATA===')
        search = input("Enter a student name OR a grade: ")

        if search.isdigit():
            grade = int(search)
            matching = [n for n, g in student_records.items() if g == grade]

            if matching:
                print(f"Students with grade {grade}: {matching}")
            else:
                print("No students found with that grade.")
        else:
            name = search.strip()
            if name in student_records:
                print(f"{name} has grade: {student_records[name]}")
            else:
                print("Student not found.")

    elif ans == '4':
        if not student_records:
            print("No records available.")
            continue

        scores = list(student_records.values())
        highest = max(scores)
        lowest = min(scores)
        average = sum(scores) / len(scores)

        print('===CLASS STATISTICS===')
        print(f'Highest Score: {highest}')
        print(f'Lowest Score: {lowest}')
        print(f'Average Grade: {average:.2f}')

        print(f'===UNIQUE SCORES===')
        unique_scores = set(scores)
        print(unique_scores)
        print(f'Total Number of Unique Scores Recorded: {len(unique_scores)}')

        print(f'===GRADE DISTRIBUTION===')
        grade_distribution = {}
        for score in scores:
            grade_distribution[score] = grade_distribution.get(score, 0) + 1
        for score in sorted(grade_distribution, key=grade_distribution.get, reverse=True):
            count = grade_distribution[score]
            plural = "students" if count!=1 else "student"
            print(f"Score {score}: {count}{plural}")

    elif ans == '5':
        print("Exiting...")
        break

    else:
        print("Invalid selection.")
