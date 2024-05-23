### 4.2.1 Parameterized functions
# A parameter is actually a variable, but there are two important factors that make parameters different and special:
    # parameters exist only inside functions in which they have been defined, and the only place where the parameter can be defined is a space between a pair of parentheses in the def statement;
    # assigning a value to the parameter is done at the time of the function's invocation, by specifying the corresponding argument.
def function(parameter):
    print(parameter)
    # parameters live inside functions (this is their natural environment)
    # arguments exist outside functions, and are carriers of values passed to corresponding parameters.
# A value for the parameter will arrive from the function's environment.
# Remember: specifying one or more parameters in a function's definition is also a requirement, and you have to fulfil it during invocation. You must provide as many arguments as there are defined parameters.

# It's legal, and possible, to have a variable named the same as a function's parameter.
def message(number):
    print("Enter a number:", number)
number = 1234
message(1) #Enter a number: 1
print(number) #1234

### 4.2.2 Positional parameter passing
def my_function(a, b, c):
    print(a, b, c)
my_function(1, 2, 3)

### 4.2.3 Keyword argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction(first_name = "James", last_name = "Bond") #Hello, my name is James Bond
introduction(last_name = "Skywalker", first_name = "Luke") #Hello, my name is Luke Skywalker

### 4.2.4 Mixing positional and keyword arguments
# You can mix both styles if you want‒there is only one unbreakable rule: you have to put positional arguments before keyword arguments.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1, 2, 3) #1 + 2 + 3 = 6
adding(c = 1, a = 2, b = 3) #2 + 3 + 1 = 6
adding(3, c = 1, b = 2) #3 + 2 + 1 = 6

### 4.2.5 Parametrized functions – more details
# It happens at times that a particular parameter's values are in use more often than others. Such arguments may have their default (predefined) values taken into consideration when their corresponding arguments have been omitted.
def introduction(first_name="John", last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe") #Hello, my name is James Doe
introduction(last_name="Hopkins") ##Hello, my name is John Hopkins