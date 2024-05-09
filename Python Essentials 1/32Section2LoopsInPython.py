### 3.2.1 Looping your code with while
# The syntactic difference with if condition is only one: you use the word while instead of the word if.
# The semantic difference is more important: when the condition is met, if performs its statements only once; while repeats the execution as long as the condition evaluates to True.
# Note: all the rules regarding indentation are applicable here, too. We'll show you this soon.

# while conditional_expression:
#     instruction_one
#     instruction_two
#     instruction_three
#     :
#     :
#     instruction_n

# It is now important to remember that:
#   if you want to execute more than one statement inside one while loop, you must (as with if) indent all the instructions in the same way;
#   an instruction or set of instructions executed inside the while loop is called the loop's body;
#   if the condition is False (equal to zero) as early as when it is tested for the first time, the body is not executed even once (note the analogy of not having to do anything if there is nothing to do);
#   the body should be able to change the condition's value, because if the condition is True at the beginning, the body might run continuously to infinity – notice that doing a thing usually decreases the number of things to do).

### 3.2.2 An infinite loop
# while True:
#     print("I'm stuck inside a loop.")
# This loop will infinitely print "I'm stuck inside a loop." on the screen.
#-------------------------------------------------------------------------
# Store the current largest number here.
largest_number = -999999999
 
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
 
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
 
# Print the largest number.
print("The largest number is:", largest_number)

### 3.2.3 The while loop: more examples
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
 
odd_numbers = 0
even_numbers = 0
 
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
 
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
 
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

## Using a counter variable to exit a loop
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

### 3.2.4   LAB   Guess the secret number
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who runs his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
# Your task is to help the magician complete the code in the editor in such a way so that the code:
#     will ask the user to enter an integer number;
#     will use a while loop;
#     will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")

### 3.2.5 Looping your code with for
# Another kind of loop available in Python comes from the observation that sometimes it's more important to count the "turns" of the loop than to check the conditions.
# Imagine that a loop's body needs to be executed exactly one hundred times. If you would like to use the while loop to do it, it may look like this:
i = 0
while i < 100:
    # do_something()
    i += 1
#there's a special loop for these kinds of tasks, and it is named for.
for i in range(100):
    # do_something()
    pass
# There are some new elements. Let us tell you about them:
#     the for keyword opens the for loop; note – there's no condition after it; you don't have to think about conditions, as they're checked internally, without any intervention;
#     any variable after the for keyword is the control variable of the loop; it counts the loop's turns, and does it automatically;
#     the in keyword introduces a syntax element describing the range of possible values being assigned to the control variable;
#     the range() function (this is a very special function) is responsible for generating all the desired values of the control variable; in our example, the function will create (we can even say that it will feed the loop with) subsequent values from the following set: 0, 1, 2 .. 97, 98, 99; note: in this case, the range() function starts its job from 0 and finishes it one step (one integer number) before the value of its argument;
#     note the pass keyword inside the loop body – it does nothing at all; it's an empty instruction – we put it here because the for loop's syntax demands at least one instruction inside the body (by the way – if, elif, else and while express the same thing)
for i in range(5):
    print("The value of i is currently", i)
# The value of i is currently 0
# The value of i is currently 1
# The value of i is currently 2
# The value of i is currently 3
# The value of i is currently 4
for i in range(2, 8):
    print("The value of i is currently", i)
# The value of i is currently 2
# The value of i is currently 3
# The value of i is currently 4
# The value of i is currently 5
# The value of i is currently 6
# The value of i is currently 7

### 3.2.6 More about the for loop and the range() function with three arguments
# The range() function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of range() looks as follows: 
# range(start, stop, step), where:
    # *start* is an optional parameter specifying the starting number of the sequence (0 by default)
    # *stop* is an optional parameter specifying the end of the sequence generated (it is not included),
    # and *step* is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)
for i in range(2, 8, 3):
    print("The value of i is currently", i)
# The value of i is currently 2
# The value of i is currently 5
# **The third argument is an increment – it's a value added to control the variable at every loop turn (as you may suspect, the default value of the increment is 1).

# Let's have a look at a short program whose task is to write some of the first powers of two:
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

### 3.2.7   LAB   Essentials of the for loop – counting mississippily
# Do you know what Mississippi is? Well, it's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
# The word Mississippi is also used for a slightly different purpose: to count mississippily.
# If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
# The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
# Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
# Use the skeleton we've provided in the editor.
import time

# Write a for loop that counts to five.
for i in range(1, 6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
# Write a print function with the final message.
print("Ready or not, here I come!")

### 3.2.8 The break and continue statements
# So far, we've treated the body of the loop as an indivisible and inseparable sequence of instructions that are performed completely at every turn of the loop. However, as a developer, you could be faced with the following choices:
#     it appears that it's unnecessary to continue the loop as a whole; you should refrain from further execution of the loop's body and go further;
#     it appears that you need to start the next turn of the loop without completing the execution of the current turn.
# Python provides two special instructions for the implementation of both these tasks. Let's say for the sake of accuracy that their existence in the language is not necessary – an experienced programmer is able to code any algorithm without these instructions. Such additions, which don't improve the language's expressive power, but only simplify the developer's work, are sometimes called syntactic candy, or syntactic sugar.
#     *break* – exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
#     *continue* – behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
# Both these words are *keywords*.
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
# ----------------------------------------
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
# ------------------------------------------
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

### 3.2.9   LAB   The break statement – Stuck in a loop
# The break statement is used to exit/terminate a loop.
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
while True:
    userInput = input("Enter a word: ")
    if userInput == "chupacabra":
        print("You've successfully left the loop.")
        break

### 3.2.10   LAB   The continue statement – the Ugly Vowel Eater
# The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
# It can be used with both the while and for loops.
# Your task here is very special: you must design a vowel eater! Write a program that uses:
    # a for loop;
    # the concept of conditional execution (if-elif-else)
    # the continue statement.
# Your program must:
    # ask the user to enter a word;
    # use user_word = user_word.upper() to convert the word entered by the user to upper case;
    # use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
    # print the uneaten letters to the screen, each one of them on a separate line.
user_word = input("Enter a word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter in ["A","E","I","O","U"]:
        continue
    print(letter)

### 3.2.11   LAB   The continue statement – the Pretty Vowel Eater
# Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab and create a better, upgraded (pretty) vowel eater! Write a program that uses:
    # a for loop;
    # the concept of conditional execution (if-elif-else)
    # the continue statement.
# Your program must:
    # ask the user to enter a word;
    # use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
    # use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
    # assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
# Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""
for letter in user_word:
    if letter in ["A","E","I","O","U"]:
        continue
    word_without_vowels += letter
print(word_without_vowels)

### 3.2.12 The while loop and the else branch
# Both loops, while and for, have one interesting (and rarely used) feature.
# Take a look at the snippet in the editor. There's something strange at the end – the else keyword.
# As you may have suspected, loops may have the else branch too, like ifs.
# The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# Output:
# 1
# 2
# 3
# 4
# else: 5
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# Output:
# else: 5

### 3.2.13 The for loop and the else branch
for i in range(5):
    print(i)
else:
    print("else:", i)
# Output:
# 0
# 1
# 2
# 3
# 4
# else: 4
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
#Output: 
# else: 111
# When the loop's body isn't executed, the control variable retains the value it had before the loop.
# Note: if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch.

### 3.2.14   LAB   Essentials of the while loop
# Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
# Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
# Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.
# Sample input:           Expected output:
# 6                       The height of the pyramid: 3
# Sample input:           Expected output:
# 20                      The height of the pyramid: 5
# Sample input:           Expected output:
# 1000                    The height of the pyramid: 44
# Sample input:           Expected output:
# 2                       The height of the pyramid: 1
blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_used = 0	

while blocks_used + height + 1 <= blocks:
    height += 1
    blocks_used += height   
print("The height of the pyramid:", height)

### 3.2.15   LAB   Collatz's hypothesis
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:
    # 1.take any non-negative and non-zero integer number and name it c0;
    # 2.if it's even, evaluate a new c0 as c0 ÷ 2;
    # 3.otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
    # 4.if c0 ≠ 1, go back to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.
# Sample input:       Expected output:    # Sample input:           Expected output:
# 15                  46                  # 16                      8
#                     46                  #                         4
#                     70                  #                         2
#                     35                  #                         1
#                     106                 #                         steps = 4
#                     53
#                     160
#                     80
#                     40
#                     20
#                     10
#                     5
#                     16
#                     8
#                     4
#                     2
#                     1
#                     steps = 17
c0 = int(input("Enter a positive number: "))
steps = 0

while c0 != 1 and c0 > 0:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)
print("steps =", steps)
#*****There are typos in the expected outputs here. I was getting crazy about this: 
#****When you input 15, how the second output of c0 will be 46? It should be 23. 
#****But when I have looked for the older versions of this exercise, I realized that in older versions, the output of my solution is the same as their expected output. 
#****Example: https://www.youtube.com/watch?v=8ykQMElaAn0&ab_channel=BrianInTech
# --------------------------------------------
# Create a for loop that counts from 0 to 10, and prints odd numbers to the screen:
for i in range(0, 11):
    if i % 2 != 0:
        print(i)
# Create a while loop that counts from 0 to 10, and prints odd numbers to the screen:
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1
# Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line:
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")
# Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen:
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
# What is the output of the following code?
n = 3
while n > 0: #3 2 1
    print(n + 1) #4 3 2
    n -= 1 #2 1 0
else:
    print(n) #0
# Output:
# 4
# 3
# 2
# 0

# What is the output of the following code?
n = range(4)
for num in n: #0 1 2 3
    print(num - 1) #-1 0 1 2
else:
    print(num)
# Output:
# -1
# 0
# 1
# 2
# 3

# What is the output of the following code?
for i in range(0, 6, 3):
    print(i)
# Output:
# 0
# 3