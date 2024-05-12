### 3.5.1 The bubble sort
#  We are going to show you a very simple algorithm, easy to understand, but unfortunately not too efficient, either. It's used very rarely, and certainly not for large and extensive lists.
# Let's say that a list can be sorted in two ways:
    # increasing (or more precisely ‒ non-decreasing) ‒ if in every pair of adjacent elements, the former element is not greater than the latter;
    # decreasing (or more precisely ‒ non-increasing) ‒ if in every pair of adjacent elements, the former element is not less than the latter.
# In the following sections, we'll sort the list in increasing order, so that the numbers will be ordered from the smallest to the largest.
# Here's the list:
[8, 10, 6, 2, 4] #We'll try to use the following approach: we'll take the first and the second elements and compare them; if we determine that they're in the wrong order (i.e., the first is greater than the second), we'll swap them round; if their order is valid, we'll do nothing. A glance at our list confirms the latter ‒ the elements 01 and 02 are in the proper order, as in 8 < 10.
#(The swapping motion with the list of elements goes on 3 passes(times) like this... ##I mean, like, what? :/)
# Now, for a moment, try to imagine the list in a slightly different way ‒ namely, like this:
10
4
2
6
8
# Look ‒ 10 is at the top. We could say that it floated up from the bottom to the surface, just like the bubble in a glass of champagne. The sorting method derives its name from the same observation ‒ it's called a bubble sort.

### 3.5.2 Sorting a list
# We solve this issue in the following way: we introduce another variable; its task is to observe if any swap has been done during the pass or not; if there is no swap, then the list is already sorted, and nothing more has to be done. We create a variable named swapped, and we assign a value of False to it, to indicate that there are no swaps. Otherwise, it will be assigned True.
my_list = [8, 10, 6, 2, 4] # list to sort 
for i in range(len(my_list) - 1): # we need (5 - 1) comparisons 
    if my_list[i] > my_list[i + 1]: # compare adjacent elements 
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # If we end up here, we have to swap the elements.
#----------------------------------------------------------------------
my_list = [8, 10, 6, 2, 4] # list to sort 
swapped = True # It's a little fake, we need it to enter the while loop. 
while swapped: 
    swapped = False # no swaps so far 
    for i in range(len(my_list) - 1): 
        if my_list[i] > my_list[i + 1]: 
            swapped = True # a swap occurred! 
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 
print(my_list)

### 3.5.3 The bubble sort – interactive version
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
#Python, however, has its own sorting mechanisms. No one needs to write their own sorts, as there is a sufficient number of ready-to-use tools. (Biz amelelik yapmışız yani şu ana dek. Söylemiyor da baştan:/)
# If you want Python to sort your list, you can do it like this:
my_list = [8, 10, 6, 2, 4] 
my_list.sort() 
print(my_list) #[2, 4, 6, 8, 10]
# There is also a list method called reverse(), which you can use to reverse the list, e.g.:
lst = [5, 3, 1, 2, 4] 
print(lst) 
lst.reverse() 
print(lst) # outputs: [4, 2, 1, 3, 5]
