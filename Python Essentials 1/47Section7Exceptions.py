### 4.7.4 The exception proves the rule
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
# Let us summarize what we talked about:
    # any part of the code placed between try and except is executed in a very special way – any error which occurs here won't terminate program execution. Instead, the control will immediately jump to the first line situated after the except keyword, and no other part of the try branch is executed;
    # the code in the except branch is activated only when an exception has been encountered inside the try block. There is no way to get there by any other means;
    # when either the try block or the except block is executed successfully, the control returns to the normal path of execution, and any code located beyond in the source file is executed as if nothing happened.

## Two exceptions after one try
# In this variant, each of the expected exceptions has its own way of handling the error, but it must be emphasized that only one of all branches can intercept the control – *if one of the branches is executed, all the other branches remain idle*.
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 

### 4.7.6 The default exception and how to use it
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
# The default except branch must be the last except branch. Always!

# You can also specify and handle multiple built-in exceptions within a single except clause:
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")
#-----------------------#
    # The program enters the while loop.
    # The try block/clause is executed. The user enters a wrong value, for example: hello!.
    # An exception occurs, and the rest of the try clause is skipped. The program jumps to the except block, executes it, and then continues running after the try-except block.
# If the user enters a correct value and no exception occurs, the subsequent instructions in the try block are executed:
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
