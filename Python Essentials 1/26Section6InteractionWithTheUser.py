### 2.6.1 The input() function
# The function is named input(). The name of the function says everything.
# The input() function is able to read data entered by the user and to return the same data to the running program.
# The program can manipulate the data, making the code truly interactive.
# Virtually all programs read and process data. A program which doesn't get a user's input is a deaf program.
# the input() function is invoked without arguments (this is the simplest way of using the function); the function will switch the console to input mode; you'll see a blinking cursor, and you'll be able to input some keystrokes, finishing off by hitting the *Enter key*; all the inputted data will be sent to your program through the function's result;
# note: you need to assign the result to a variable; this is crucial ‒ missing out this step will cause the entered data to be lost;
# then we use the print() function to output the data we get, with some additional remarks.
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

### 2.6.2 The input() function with an argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
#This variant of the input() invocation simplifies the code and makes it clearer.

### 2.6.3 The result of the input() function
#We've said it already, but it must be unambiguously stated once again: the result of the input() function is a string.
#A string containing all the characters the user enters from the keyboard. It is not an integer or a float.
# This means that you mustn't use it as an argument of any arithmetic operation, e.g.
anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
### 2.6.4 The input() function – prohibited operations
#ERROR: Traceback (most recent call last):
#   File "main.py", line 2, in 
#     something = anything ** 2.0
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

### 2.6.5 Type casting (type conversions)
#Python offers two simple functions to specify a type of data and solve this problem ‒ here they are: int() and float().
# the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer
# the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something) #7.0 to the power of 2 is 49.0

### 2.6.6 More about input() and type casting
# Having a team consisting of the trio input()-int()-float() opens up lots of new possibilities.
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
# The program asks the user for the lengths of both legs, evaluates the hypotenuse and prints the result. Run it and try to input some negative values.
# The program, unfortunately, doesn't react to this obvious error. Let's ignore this weakness for now. We'll come back to it soon.

### 2.6.7 String operators
# We want to show you that they have a second function. They are able to do something more than just add and multiply.
# The + (plus) sign, when applied to two strings, becomes a concatenation operator:
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# Note: using + to concatenate strings lets you construct the output in a more precise way than with a pure print() function, even if enriched with the end= and sep= keyword arguments.

##Replication
# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:
# string * number
# number * string
# Example:
# "James" * 3 gives "JamesJamesJames"
# 3 * "an" gives "ananan"
# 5 * "2" (or "2" * 5) gives "22222" (not 10!)

#  ***Remember  
# A number less than or equal to zero produces an empty string.
# This simple program "draws" a rectangle, making use of an old operator (+) in a new role:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

### 2.6.8 Type conversions once again
# You can also convert a number into a string, which is way easier and safer ‒ this kind of operation is always possible.
# str(number)
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#We've modified it a bit to show you how the str() function works. Thanks to this, we can pass the whole result to the print() function as one string, forgetting about the commas.

# input a float value for variable a here
a = float(input("Input a number please:"))
# input a float value for variable b here
b = float(input("Input another number please:"))

### 2.6.9   LAB   Simple input and output
# output the result of addition here
print("The addition result of the numbers " + str(a+b))
# output the result of subtraction here
print("The subtraction result of the numbers " + str(a-b))
# output the result of multiplication here
print("The multiplication result of the numbers " + str(a*b))
# output the result of division here
print("The division result of the numbers " + str(a/b))
print("\nThat's all, folks!")

### 2.6.10   LAB   Operators and expressions
# Sample input:       Expected output:
# 1                   y = 0.6000000000000001
# Sample input:       Expected output:
# 10                  y = 0.09901951266867294
# Sample input:       Expected output:
# 100                 y = 0.009999000199950014
# Sample input:       Expected output:
# -5                  y = -0.19258202567760344
x = float(input("Enter value for x: "))

# Write your code here.
y= str(1/(x+1/(x+1/(x+1/x))))
print("y =", y)

### 2.6.11   LAB   Operators and expressions – 2
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
# Sample input:       Expected output:
# 12                  13:16
# 17
# 59

# Sample input:       Expected output:
# 23                  10:40
# 58
# 642

# Sample input:       Expected output:
# 0                   1:0
# 1
# 2939
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
