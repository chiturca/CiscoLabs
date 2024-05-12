### 3.6.1 The inner life of lists
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2) #[2]
# Lists (and many other complex Python entities) are stored in different ways than ordinary (scalar) variables.
# You could say that:
    # the name of an ordinary variable is the name of its content;
    # the name of a list is the name of a memory location where the list is stored.
# The assignment: list_2 = list_1 copies the name of the array, not its contents. In effect, the two names (list_1 and list_2) identify the same location in the computer memory. Modifying one of them affects the other, and vice versa.
# How do you cope with that?

### 3.6.2 Powerful slices
# Fortunately, the solution is at your fingertips ‒ it's called a slice.
# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
# It actually copies the list's contents, not the list's name.
# This is exactly what you need. Take a look at the snippet below:
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2) #[1]
# This inconspicuous part of the code described as [:] is able to produce a brand new list.

# One of the most general forms of the slice looks as follows:
    # my_list[start:end]
# As you can see, it resembles indexing, but the colon inside makes a big difference.
# A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from start to end - 1.
# Note: not to end but to *end - 1*. An element with an index equal to end is the first element which does not take part in the slicing.
# Using negative values for both start and end is possible (just like in indexing).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list) #[8, 6]

### 3.6.3 Slices – negative indices
    # start is the index of the first element included in the slice;
    # end is the index of the first element not included in the slice.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) #[8, 6, 4]

# If the start specifies an element lying further than the one described by the end (from the list's beginning), the slice will be empty:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) #[]

# my_list[:end] == my_list[0:end]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list) #[10, 8, 6]

# my_list[start:] == my_list[start:len(my_list)]
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list) #[4, 2]

## More about the del instruction
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]
# Note: in this case, the slice doesn't produce any new list!

# Deleting all the elements at once is possible too:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list) #[]

### 3.6.4 The in and not in operators
    # elem in my_list      #checks if a given element (its left argument) is currently stored somewhere inside the list (the right argument) ‒ the operator returns True in this case.
    # elem not in my_list  #checks if a given element (its left argument) is absent in a list ‒ the operator returns True in this case.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest) #17
#---------------------------------------
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print(largest) #17
# If you need to save computer power, you can use a slice:
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list[1:]:
    if i > largest:
        largest = i
print(largest) #17

# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# The question is: how many numbers have you hit?
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
for number in bets:
    if number in drawn:
        hits += 1
print(hits) #4

# Imagine a list ‒ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code ‒ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Hint: we encourage you to create a new list as a temporary work area ‒ you don't need to update the list in situ.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# Write your code here.
my_list.sort()
new_list = []
for i in range(len(my_list)):
    if i == len(my_list) - 1 or my_list[i] != my_list[i + 1]:
        new_list.append(my_list[i])
#
print("The list with unique elements only:")
print(new_list) #[1, 2, 4, 6, 9]
