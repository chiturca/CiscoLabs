### 4.3.1 Effects and results: the return instruction
# To get functions to return a value (but not only for this purpose) you use the return instruction.
# Note: it's a Python keyword.
# The return instruction has two different variants ‒ let's consider them separately.

##return without an expression
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")
happy_new_year()
# Three...
# Two...
# One...
# Happy New Year!
happy_new_year(False)
# Three...
# Two...
# One...

### return with an expression
# There are two consequences of using it:
    # it causes the immediate termination of the function's execution (nothing new compared to the first variant)
    # moreover, the function will evaluate the expression's value and will return it (hence the name once again) as the function's result.
def boring_function():
    return 123
x = boring_function()
print("The boring_function has returned its result. It's:", x)
# The boring_function has returned its result. It's: 123
# The return instruction, enriched with the expression (the expression is very simple here), "transports" the expression's value to the place where the function has been invoked.
    # The result may be freely used here, e.g., to be assigned to a variable.
    # It may also be completely ignored and lost without a trace.
def boring_function():
    print("'Boredom Mode' ON.")
    return 123
print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")
# This lesson is interesting!
# 'Boredom Mode' ON.
# This lesson is boring...

# Don't forget:
    # you are always allowed to ignore the function's result, and be satisfied with the function's effect (if the function has any)
    # if a function is intended to return a useful result, it must contain the second variant of the return instruction.

### 4.3.2 A few words about None
# Note: None is a keyword.
# There are only two kinds of circumstances when None can be safely used:
    # when you assign it to a variable (or return it as a function's result)
    # when you compare it with a variable to diagnose its internal state.
value = None
if value is None:
    print("Sorry, you don't carry any value")
# **Don't forget this: if a function doesn't return a certain value using a return expression clause, it is assumed that it implicitly returns None.
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2)) #True
print(strange_function(1)) #None

### 4.3.3 Effects and results: lists and functions
# Question: may a list be sent to a function as an argument? Yes:
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3])) #12
print(list_sum(5)) #TypeError: 'int' object is not iterable

# Question: may a list be a function result? Yes:
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5)) #[4, 3, 2, 1, 0]

### 4.3.4   LAB   A leap year: writing your own functions
# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
# The seed of the function is already shown in the skeleton code in the editor.
# Note: we've also prepared a short testing code, which you can use to test your function.
# The code uses two lists ‒ one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.
def is_year_leap(year):
    if year % 4 == 0:  # Leap years are divisible by 4
        if year % 100 == 0:  # Except for years that are divisible by 100
            if year % 400 == 0:  # But including years that are divisible by 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

### 4.3.5   LAB   How many days: writing and using your own functions
# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).
# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return 29
    return days_per_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

### 4.3.6   LAB   Day of the year: writing and using your own functions
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return 29
    return days_per_month[month - 1]

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    MD = days_in_month(year, month)
    if day >= 1 and day <= MD:
        return days + day
    else:
        return None
print(day_of_year(2000, 12, 31))  # Output: 366 (leap year)
print(day_of_year(2021, 1, 15))   # Output: 15
print(day_of_year(2022, 2, 29))   # Output: None (invalid day for non-leap year)

### 4.3.7   LAB   Prime numbers ‒ how to find them
# A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
# Complicated? Not at all. For example, 8 isn't a prime number, as you can divide it by 2 and 4 (we can't use divisors equal to 1 and 8, as the definition prohibits this).
# On the other hand, 7 is a prime number, as we can't find any legal divisors for it.
# Your task is to write a function checking whether a number is prime or not.
# The function:
    # is called is_prime;
    # takes one argument (the value to check)
    # returns True if the argument is a prime number, and False otherwise.
# Hint: try to divide the argument by all subsequent values (starting from 2) and check the remainder ‒ if it's zero, your number cannot be a prime; think carefully about when you should stop the process.
# If you need to know the square root of any value, you can utilize the ** operator. Remember: the square root of x is the same as x**0.5

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)): #If you find factors other than 1 and the number itself, it is not prime. 
        if num % i == 0:                    #That's why we are using sqr root of the num.
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

### 4.3.8   LAB   Converting fuel consumption
# A car's fuel consumption may be expressed in many different ways. 
#For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.
# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.
# The functions:
    # are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
    # take one argument (the value corresponding to their names)
    # Complete the code in the editor and run it to check whether your output is the same as ours.
# Here is some information to help you:
    # 1 American mile = 1609.344 metres;
    # 1 American gallon = 3.785411784 litres.
mile = 1609.344 #metres
gallon = 3.785411784 #liters
def liters_100km_to_miles_gallon(liters):
    miles = 100 * (mile / 1000) # Convert 100 kilometers to miles
    mpg = miles / (liters / gallon) # Calculate miles per gallon
    return mpg

def miles_gallon_to_liters_100km(miles):
    km = miles * (mile/1000) # Convert miles to kilometer
    liters_100km = gallon / (km / 100) # Calculate liters per 100 kilometers
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))