import numbers

def print_numbers(n):
    numbers= range(n)
    for number in numbers:
        print (number)
 # print numbers(100)
 # print numbers(1000) 


    def  print_even_numbers(n):
        numbers = range(n)
        for number in numbers:
            if number %2 ==0:
                print(number)
# print_even_numbers(100)
# print_even_numbers(1000)


    def odd_or_even(n):
        numbers= range(n)
        for number in numbers:
            if number %2==0:
                print(f"{number} is even")
            else:
                print(f"{number} is odd")

# odd_or_even(100)
# odd_or_even(1000)
                

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(f"{number} is divisible by 2") 
        elif number%3 == 0:
            print(f"{number} is divisible by 3")               
        elif number%5 == 0:
            print(f"{number} is divisible by 5")
        elif number%7 == 0:
            print(f"{number} is divisible by 7")
        else: 
            print(f"{number} is not divisible by 2, 3, 5 and 7")   

def countdown(n):
    while n>0:
        print(n)
        n-=1


def countdown_to_five(n):
    while n>0:
        print(n)
        if n==5:
           break
        n-=1
# n-=1 - used when one owants to stop the looping and still print the previous numbers
        
# divisible by 7
def divisible_by_seven(n):
    x=1
    while x>=n:
        x+=1
        if x%7!=0:
            continue
        print(x)

# printing the following divisibilities
def fizzbuzz(n):
    numbers= range(n)
    for number in numbers:
        if number%3==0:
           print("fizz")
        elif number%5==0:
           print("BUzz")
        else: 
           print("fizzbuzz")

# checking for the odd numbers that are divisible by 7
def print_even_numbers(n):
        x=0
        while x<=n:
            x+=1
            if x%2!=0:
                continue
            print(x)

#  checking ranges
def check_numbers(n):
    numbers=range(2,200)
    for number in numbers:
        if number%3==0:
           print("fizz")
        elif number%5==0:
           print("BUzz")
        else: 
           print("fizzbuzz")


    

