print("Welcome to Grade Calculator 2025")
reply = "Yes"
while True : 
    score = int(input("Enter your score (0-100): ")) 
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"
    #added some extra options for the comment for each grade type 
    print(f"Your grade is: {grade}") 
    if grade == "A" :
        print("Excellent work!""")
    if grade == "B" :
        print("Well done!")
    if grade == "C" :
        print("With some more study, you could do great")
    if grade == "D" :
        print("You need to spend more time revising")
    if grade == "E" :
        print("You could do much better with more study, and less parties")
    reply = str(input("Would you like to calculate another grade? Yes/No "))
    if reply == "Yes" :
        continue
    elif reply == "No" :
        break
print("Thank you for using Grade Calculator 2025. Goodbye.")
