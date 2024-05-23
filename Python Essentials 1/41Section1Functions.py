### 4.1.4 Your first function
print("Enter a value: ")
a = int(input())
print("Enter a value: ")
b = int(input())
print("Enter a value: ")
c = int(input())
# This is what the simplest function definition looks like:
    # def function_name():
    #     function_body
        # it always starts with the keyword def (for define)
        # next after def goes the name of the function (the rules for naming functions are exactly the same as for naming variables)
        # after the function name, there's a place for a pair of parentheses (they contain nothing here, but that will change soon)
        # the line has to be ended with a colon;
        # the line directly after def begins the function body ‒ a couple (at least one) of necessarily nested instructions, which will be executed every time the function is invoked; note: the function ends where the nesting ends, so you have to be careful.
def message():
    print("Enter a value: ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

### 4.1.5 How functions work
    # when you invoke a function, Python remembers the place where it happened and jumps into the invoked function;
    # the body of the function is then executed;
    # reaching the end of the function forces Python to return to the place directly after the point of invocation
# There are two, very important, catches. Here's the first of them:
    # You mustn't invoke a function which is not known at the moment of invocation.
# Remember - Python reads your code from top to bottom. It's not going to look ahead in order to find a function you forgot to put in the right place ("right" means "before invocation".)
print("We start here.")
message() #NameError: name 'message' is not defined
print("We end here.")
def message():
    print("Enter a value: ")

    # You mustn't have a function and a variable of the same name.
def message():
    print("Enter a value: ")
message = 1 #Assigning a value to the name message causes Python to forget its previous role. The function named message becomes unavailable.

# There are at least four basic types of functions in Python:
    # *built-in functions* which are an integral part of Python (such as the print() function). You can see a complete list of built-in Python functions at https://docs.python.org/3/library/functions.html.
    # the ones that come from *pre-installed modules* (you'll learn about them in the Python Essentials 2 course)
    # *user-defined functions* which are written by users for users ‒ you can write your own functions and use them freely in your code,
    # the *lambda functions* (you'll learn about them in the Python Essentials 2 course.)
