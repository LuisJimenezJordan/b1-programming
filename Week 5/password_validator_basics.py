import random
import string

def check_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)

def has_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)

def has_digit(password):
    return any(char in string.digits for char in password)

def has_special_char(password):
    return any(char in string.punctuation for char in password)

def validate_password(password):
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special': has_special_char(password)
    }
    results['is_valid'] = all(results.values())
    return results

password = input("Enter password to validate: ")

results = validate_password(password)

print("\n" + "=" * 50)
print("VALIDATION RESULTS")
print("=" * 50)

check_symbol = "✓" if results['min_length'] else "x"
print(f"{check_symbol} Minimum length is 8 or more characters: {results['min_length']}")

check_symbol = "✓" if results['has_uppercase'] else "x"
print(f"{check_symbol} Contains at least one uppercase letter: {results['has_uppercase']}")

check_symbol = "✓" if results['has_lowercase'] else "x"
print(f"{check_symbol} Contains at least one lowercase letter: {results['has_lowercase']}")

check_symbol = "✓" if results['has_digit'] else "x"
print(f"{check_symbol} Contains a digit: {results['has_digit']}")

check_symbol = "✓" if results['has_special'] else "x"
print(f"{check_symbol} Contains a special character: {results['has_special']}")

print("\n" + "=" * 50)
if results['is_valid']:
    print("✓ PASSWORD IS STRONG!")
else:
    print("x PASSWORD IS WEAK - Please address failed requirements")
print("=" * 50)

#print(f"Suggestion: Your password could benefit from adding a random character such as '{random.choice(string.punctuation)}'")