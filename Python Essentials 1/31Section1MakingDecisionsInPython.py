### 3.1.1 Questions and answers
# A programmer writes a program and the program asks questions.
# A computer executes the program and provides the answers. The program must be able to react according to the received answers.
# Fortunately, computers know only two kinds of answers:
# yes, this is true;
# no, this is false.

### 3.1.2 Comparison: equality operator
# 2 == 2 => True - of course, 2 is equal to 2. Python will answer True
# 2 == 2. => This question is not as easy as the first one. Luckily, Python is able to convert the integer value into its real equivalent, and consequently, the answer is True.
# 1 == 2 => This should be easy. The answer will be (or rather, always is) False.

### 3.1.4 Operators
## Equality: the equal to operator (==)
var = 0  # Assigning 0 to var
print(var == 0) #True
var = 1  # Assigning 1 to var
print(var == 0) #False

## Inequality: the not equal to operator (!=)
var = 0  # Assigning 0 to var
print(var != 0) #False
var = 1  # Assigning 1 to var
print(var != 0) #True

## Comparison operators: greater than
# black_sheep > white_sheep

## Comparison operators: greater than or equal to
# centigrade_outside >= 0.0  

## Comparison operators: less than/less than or equal to
# current_velocity_mph < 85
# current_velocity_mph <= 85

### 3.1.5 Making use of the answers
# Priority	Operator	
# 1	        +, -	unary
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	binary
# 5	        <, <=, >, >=	
# 6	        ==, !=	

### 3.1.6   LAB   Variables ‒ Questions and answers
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
n = int(input("Enter a number: "))
print(n >= 100)

### 3.1.7 Conditions and conditional execution
# syntax:
# if true_or_not:
#     do_this_if_true

# This conditional statement consists of the following, strictly necessary, elements in this and this order only:
# the if keyword;
# one or more white spaces;
# an expression (a question or an answer) whose value will be interpreted solely in terms of True (when its value is non-zero) and False (when it is equal to zero);
# a colon followed by a newline;
# an indented instruction or set of instructions (at least one instruction is absolutely required); the indentation may be achieved in two ways – by inserting a particular number of spaces (the recommendation is to use four spaces of indentation), or by using the tab character; note: if there is more than one instruction in the indented part, the indentation should be the same in all lines; even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations exactly the same – Python 3 does not allow the mixing of spaces and tabs for indentation.

# How does that statement work?
# If the true_or_not expression represents the truth (i.e., its value is not equal to zero), the indented statement(s) will be executed;
# if the true_or_not expression does not represent the truth (i.e., its value is equal to zero), the indented statement(s) will be omitted (ignored), and the next executed instruction will be the one after the original indentation level.

## Conditional execution: the if statement
# if sheep_counter >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()
# As you can see, making a bed, taking a shower and falling asleep and dreaming are all executed conditionally – when sheep_counter reaches the desired limit.
# Feeding the sheepdogs, however, is always done (i.e., the feed_the_sheepdogs() function is not indented and does not belong to the if block, which means it is always executed.)

## Conditional execution: the if-else statement
# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

# if the_weather_is_good:
#     go_for_a_walk()
#     have_fun()
# else:
#     go_to_a_theater()
#     enjoy_the_movie()
# have_lunch()

## Nested if-else statements
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

## The elif statement
# if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()

### 3.1.8 Analyzing code samples
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)
# Note: if any of the if-elif-else branches contains just one instruction, you may code it in a more comprehensive form (you don't need to make an indented line after the keyword, but just continue the line after the colon).
# This style, however, may be misleading, and we're not going to use it in our future programs, but it's definitely worth knowing if you want to read and understand someone else's programs.
#--------------------------------------------------
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
 
# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2
 
# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3
 
# Print the result
print("The largest number is:", largest_number)

### 3.1.9 Pseudocode and introduction to loops
# We'll ignore the requirements of Python syntax for now, and try to analyze the problem without thinking about the real programming. In other words, we'll try to write the algorithm, and when we're happy with it, we'll implement it.
# In this case, we'll use a kind of notation which is not an actual programming language (it can be neither compiled nor executed), but it is formalized, concise and readable. It's called pseudocode.
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

# The trick is based on the assumption that any part of the code can be performed more than once – precisely, as many times as needed.
# Performing a certain part of the code more than once is called a loop. The meaning of this term is probably obvious to you.
# Lines 02 through 08 make a loop. We'll pass through them as many times as needed to review all the entered values.
# Can you use a similar structure in a program written in Python? Yes, you can.
# Python often comes with a lot of built-in functions that will do the work for you. For example, to find the largest number of all, you can use a Python built-in function called max(). You can use it with multiple arguments. Analyze the code below:
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
 
largest_number = max(number1, number2, number3)
 
# Print the result.
print("The largest number is:", largest_number)

### 3.1.10   LAB   Comparison operators and conditional execution
# Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.
# Write a program that utilizes the concept of conditional execution, takes a string as input, and:
# prints the sentence "Yes - Spathiphyllum is the best 
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
name = input("Enter flower name: ")

if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")

### 3.1.11   LAB   Essentials of the if-else statement
# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you – you'll find it in the skeleton code in the editor.
# Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

### 3.1.12   LAB   Essentials of the if-elif-else statement
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
#-------------------------
x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z) #True
print((y - 5) == x) #False
#-------------------------
x = 10
 
if x == 10:
    print(x == 10) #True
if x > 5:
    print(x > 5) #True
if x < 10:
    print(x < 10)
else:
    print("else")
#else
