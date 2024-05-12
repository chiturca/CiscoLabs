numbers = [10, 5, 7, 2, 1]
### 3.4.3 Accessing list content
## The len() function
# The length of a list may vary during execution. New elements may be added to the list, while others may be removed from it. This means that the list is a very dynamic entity.

### 3.4.4 Removing elements from a list
del numbers[1]
print(len(numbers))
print(numbers)

### 3.4.5 Negative indices are legal
# An element with an index equal to -1 is the last one in the list.
# Similarly, the element with an index equal to -2 is the one before last in the list.

### 3.4.6   LAB   The basics of lists
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
userInput = int(input("Please enter a number: "))
hat_list[2] = userInput
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print("Length of the existing list:",len(hat_list))
print(hat_list)

### 3.4.7 Functions vs. methods
# A method is a specific kind of function ‒ it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
# A function doesn't belong to any data ‒ it gets data, it may create new data and it (generally) produces a result.
    # result = function(arg) #function invocation
# A method does all these things, but is also able to change the state of a selected entity.
    # result = data.method(arg) # method invocation
# A method is owned by the data it works for, while a function is owned by the whole code.
# This also means that invoking a method requires some specification of the data from which the method is invoked.
# The method will behave like a function, but can do something more ‒ it can change the internal state of the data from which it has been invoked.
# we're going to show you how to add new elements to an existing list. This can be done with methods owned by all the lists, not by functions.

### 3.4.8 Adding elements to a list: append() and insert()
# *list.append(value)*  #It takes its argument's value and puts it at the end of the list which owns the method.The list's length then increases by one.
# *list.insert(location, value)* 
# It takes two arguments:
    # the first shows the required location of the element to be inserted; note: all the existing elements that occupy locations to the right of the new element (including the one at the indicated position) are shifted to the right, in order to make space for the new element;
    # the second is the element to be inserted.
numbers = [111, 7, 2, 1]
print(len(numbers)) #4
print(numbers) #[111, 7, 2, 1]
###
numbers.append(4)
print(len(numbers)) #5
print(numbers) #[111, 7, 2, 1, 4]
###
numbers.insert(1, 333)
print(numbers) #[111, 333, 7, 2, 1, 4]
#-------------------------------------
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)
print(my_list) #[1, 2, 3, 4, 5]
###
my_list = [] 
for i in range(5):
    my_list.insert(0, i + 1)
print(my_list) #[5, 4, 3, 2, 1]
# You should get the same sequence, but in reverse order (this is the merit of using the insert() method).

### 3.4.10 Lists in action
# Let's leave lists aside for a short moment and look at one intriguing issue.
# Imagine that you need to rearrange the elements of a list, i.e., reverse the order of the elements: the first and the fifth as well as the second and fourth elements will be swapped. The third one will remain untouched.
# Question: how can you swap the values of two variables?

# Take a look at the snippet:
variable_1 = 1
variable_2 = 2
 
variable_2 = variable_1
variable_1 = variable_2
 
# If you do something like this, you would lose the value previously stored in variable_2. Changing the order of the assignments will not help. You need a third variable that serves as an auxiliary storage.
variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
 
# Python offers a more convenient way of doing the swap – take a look:
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1
 
# Clear, effective and elegant - isn't it?   ##Is it, really?
# Now you can easily swap the list's elements to reverse their order:
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
# Output: [5, 3, 8, 1, 10]

# Will it still be acceptable with a list containing 100 elements? No, it won't.
# Can you use the for loop to do the same thing automatically, irrespective of the list's length? Yes, you can:
for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]
 
print(my_list)
# Note:
    # we've assigned the length variable with the current list's length (this makes our code a bit clearer and shorter)
    # we've launched the for loop to run through its body length // 2 times (this works well for lists with both even and odd lengths, because when the list contains an odd number of elements, the middle one remains untouched)
    # we've swapped the ith element (from the beginning of the list) with the one with an index equal to (length - i - 1) (from the end of the list); in our example, for i equal to 0 the (length - i - 1) gives 4; for i equal to 1, it gives 3 ‒ this is exactly what we needed.

### 3.4.11   LAB   The basics of lists ‒ the Beatles
# step 1: create an empty list named beatles;
beatles = []
print("Step 1:", beatles)
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
newMembers =["Stu Sutcliffe", "Pete Best"]
for i in newMembers:
    input(f"Add {i} to the list by entering the name: ")
    beatles.append(i)
print("Step 3:", beatles)
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)
# testing list legth
print("The Fab", len(beatles))