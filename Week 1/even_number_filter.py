numbers = range(10)
#used the range function to make things cleaner

for number in numbers:
    if number % 2 != 0:
        # Skip odd numbers 
        continue
    print (number) 
    