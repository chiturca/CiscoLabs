### 2.4.2 Variable names
# If you want to give a name to a variable, you must follow some strict rules:
# the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# the name of the variable must begin with a letter;
# the underscore character is a letter;
# upper- and lower-case letters are treated as different (a little differently than in the real world – Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
# the name of the variable must not be any of Python's reserved words (the keywords – we'll explain more about this soon).
# Note that the same restrictions apply to function names.

# Python does not impose restrictions on the length of variable names, but that doesn't mean that a long variable name is always better than a short one.

## Here are some correct, but not always convenient variable names:
# MyVariable
# i
# l
# t34
# Exchange_Rate
# counter
# days_to_christmas
# TheNameIsTooLongAndHardlyReadable
# _
## These variable names are also correct:
# Adiós_Señora
# sûr_la_mer
# Einbahnstraße
# переменная.
# Python lets you use not only Latin letters but also characters specific to languages that use other alphabets.

## And now for some incorrect names:
# 10t (does not begin with a letter)
# !important (does not begin with a letter)
# exchange rate (contains a space).

## Keywords
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# They are called keywords or (more precisely) reserved keywords. They are reserved because you mustn't use them as names: neither for your variables, nor functions, nor any other named entities you want to create.

### 2.4.7   LAB   Variables
#Your task is to:
# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to the addition of the three previous variables.
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.
john=3
mary=5
adam=6
print(john,",",mary,",",adam)
total_apples=john+mary+adam
print(total_apples)

###2.4.8 Shortcut operators
# Expression	            Shortcut operator
# i = i + 2 * j             i += 2 * j
# var = var / 2             var /= 2
# rem = rem % 10            rem %= 10
# j = j - (i + var + rem)   j -= (i + var + rem)
# x = x ** 2                x **= 2

###2.4.9   LAB   Variables ‒ a simple converter
# Miles and kilometers are units of length or distance.
# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
# miles to kilometers;
# kilometers to miles.
# Pay particular attention to what is going on inside the print() function. Analyze how we provide multiple arguments to the function, and how we output the expected data.
# Note that some of the arguments inside the print() function are strings (e.g., "miles is", whereas some other are variables (e.g., miles).
#   Tip  
# There's one more interesting thing happening there. Can you see another function inside the print() function? It's the round() function. Its job is to round the outputted result to the number of decimal places specified in the parentheses, and return a float (inside the round() function you can find the variable name, a comma, and the number of decimal places we're aiming for). 
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

###2.4.10   LAB   Operators and expressions
# Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:
# 3x3 - 2x2 + 3x - 1
# The result should be assigned to y.
# Remember that classical algebraic notation likes to omit the multiplication operator ‒ you need to use it explicitly. Note how we change data type to make sure that x is of type float.
# Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the x variable (by hardcoding it). Don't be discouraged by any initial failures. Be persistent and inquisitive.
# Sample input    Sample output
# x = 0           y = -1.0
# x = 1           y = 3.0
# x = -1          y = -9.0
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

#----------------------
a = 6
b = 3
a /= 2 * b #a = a/(2*b)
print(a)