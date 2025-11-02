login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("john", "failed"),
    ("greg", "failed"),
    ("alice", "failed")
]

print(f"Would you like to run Security Check?")
proceed = input("Please type 'YES' to run: ")
if proceed == "YES":
    print(f'Checking login attempts...')
    users = []
    for username, status in login_attempts:
        if username not in users:
            users.append(username)

    for user in users:
        failed_count = login_attempts.count((user, "failed"))
        if failed_count >= 3:
            print("ALERT:", user, "has", failed_count, "failed login attempts!")
    print(f'Security check complete.')

else: 
    print(f'Exiting...')
