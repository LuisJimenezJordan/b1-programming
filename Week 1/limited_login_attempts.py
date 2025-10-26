correct_pin = "9387"
attempts = 0
max_attempts = 5
login_successful = False
while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    entered_pin = input("Enter your four digit PIN: ")

    if entered_pin == correct_pin:
        print("PIN accepted! Welcome.")
        login_successful = True
        break # Exit the loop if PIN is correct
    else:
        print("Incorrect PIN.")
        attempts += 1

if not login_successful:
    print("Too many incorrect attempts. Account locked.")