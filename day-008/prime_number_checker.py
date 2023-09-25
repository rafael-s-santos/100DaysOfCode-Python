#Write your code below this line 👇
def prime_checker(number):
    range_number = range(number)
    validator = 0
    for num in range_number:
        if (number % (num + 1)) == 0:
            validator += 1
    if validator == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
