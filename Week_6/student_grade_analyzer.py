student_records = []
stats = {}

print("Welcome to Student Grade Analyzer")

while True:
    print("\nGrade Analyzer Menu:")
    print("1. Enter Grades for One Student")
    print("2. Enter Grades for Multiple Students")
    print("3. View Student Records")
    print("4. View Class Statistics")
    print("5. Exit")

    ans = input("Enter your choice: ")

    if ans == '1':
        print("Enter Student Data:")
        name = input(" Student Name: ")
        score = int(input(" Score: "))
        student_records.append((name, score))

    elif ans == '2':
        print("Enter Student data for entire class (6 students)")
        for i in range(1, 7):
            print(f"Enter Student Information #{i}:")
            name = input(" Student Name: ")
            score = int(input(" Score: "))
            student_records.append((name, score))

    elif ans == '3':
        if not student_records:
            print("No records available.")
            continue
            
        print('=== STUDENT RECORDS ===')
        for index, (name, score) in enumerate(student_records, start=1):
            print(f'{index}. {name}: {score}')

    elif ans == '4':
        if not student_records:
            print("No records available.")
            continue

        # Extract scores
        scores = [score for name, score in student_records]
        
        # Calculate and store statistics in dictionary
        stats['highest'] = max(scores)
        stats['lowest'] = min(scores)
        stats['average'] = sum(scores) / len(scores)

        print('=== CLASS STATISTICS ===')
        print(f"Highest Score: {stats['highest']}")
        print(f"Lowest Score: {stats['lowest']}")
        print(f"Average Score: {stats['average']:.2f}")

        print('\n=== UNIQUE SCORES ===')
        unique_scores = set(scores)
        print(unique_scores)
        print(f'Total unique scores: {len(unique_scores)}')

        print('\n=== GRADE DISTRIBUTION ===')
        grade_distribution = {}
        for score in scores:
            grade_distribution[score] = grade_distribution.get(score, 0) + 1
        
        for score in sorted(grade_distribution, key=grade_distribution.get, reverse=True):
            count = grade_distribution[score]
            plural = "students" if count != 1 else "student"
            print(f"Score {score}: {count} {plural}")

    elif ans == '5':
        print("Exiting...")
        break

    else:
        print("Invalid selection.")