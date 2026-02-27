passwords = [ "Pass123","SecurePassword1", "weak","MyP@ssw0rd", "NOLOWER123"]

compliant = 0
noncompliant = 0

print(f"Would you like to check password options for validity?")
proceed = input("Please type 'YES' to run: ")
if proceed == "YES":
    print(f'Checking passwords against parameters...')

    for option in passwords:
        valid = True
        problems = []

        if len(option) <8 :
            problems.append("Too few characters")
            valid = False

        if option.isupper():
            problems.append("Only contains uppercase letters")
            valid = False

        if option.islower():
            problems.append ("Only contains lowercase letters")
            valid = False
       
        if not any(chr.isdigit() for chr in option):
            problems.append ("Contains no digits")
            valid = False
    
        if valid == True:
            print(f"SUCCESS:'{option}' satisfies password restrictions")
            compliant +=1

        if valid == False:
            print(f"ERROR:'{option}'is invalid. {', '.join(problems)}")
            noncompliant +=1

    print(f"There are {compliant} compliant passwords, and {noncompliant} noncompliant passwords")
    print(f'Password checker complete. Exiting...')

else: 
    print(f'Exiting...')