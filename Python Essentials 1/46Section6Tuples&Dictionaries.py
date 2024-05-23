### 4.6.1 Sequence types and mutability
# Before we start talking about tuples and dictionaries, we have to introduce two important concepts: sequence types and mutability.
# A sequence type is a type of data in Python which is able to store more than one value (or less than one, as a sequence may be empty), and these values can be sequentially (hence the name) browsed, element by element.
# As the for loop is a tool especially designed to iterate through sequences, we can express the definition as: a sequence is data which can be scanned by the for loop.
# You've encountered one Python sequence so far − the list. The list is a classic example of a Python sequence, although there are some other sequences worth mentioning, and we're going to present them to you now.
# The second notion − mutability − is a property of any Python data that describes its readiness to be freely changed during program execution. There are two kinds of Python data: mutable and immutable.
# Mutable data can be freely updated at any time − we call such an operation in situ.
# In situ is a Latin phrase that translates as literally in position. For example, the following instruction modifies the data in situ:
list.append(1)
# Immutable data cannot be modified in this way.
# Imagine that a list can only be assigned and read over. You would be able neither to append an element to it, nor remove any element from it. This means that appending an element to the end of the list would require the recreation of the list from scratch.
# You would have to build a completely new list, consisting of the all elements of the already existing list, plus the new element.
# The data type we want to tell you about now is a tuple. A tuple is an immutable sequence type. It can behave like a list, but it can't be modified in situ.

### 4.6.2 Tuples
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
print(tuple_1) #(1, 2, 4, 8)
print(tuple_2) #(1.0, 0.5, 0.25, 0.125)
# Note: each tuple element may be of a different type (floating-point, integer, or any other not-as-yet-introduced kind of data).

## How to create a tuple
empty_tuple = ()
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1., 
#Removing the commas won't spoil the program in any syntactical sense, but you will instead get two single variables, not tuples.
my_tuple = (1, 10, 100, 1000)
print(my_tuple[0]) #1
print(my_tuple[-1]) #1000
print(my_tuple[1:]) #(10,100,1000)
print(my_tuple[:-2]) #(1,10)
for elem in my_tuple:
    print(elem)
# What else can tuples do for you?
    # the len() function accepts tuples, and returns the number of elements contained inside;
    # the + operator can join tuples together (we've shown you this already)
    # the * operator can multiply tuples, just like lists;
    # the in and not in operators work in the same way as in lists.
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
print(len(t2)) #9
print(t1) #(1, 10, 100, 1000, 10000)
print(t2) #(1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple) #True
print(-10 not in my_tuple) #True
# ---------------------------- #
var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3) #(2,) (3, 123) (1,)
# It shows three tuples interacting − in effect, the values stored in them "circulate" − t1 becomes t2, t2 becomes t3, and t3 becomes t1.
# ***Note: the example presents one more important fact: a tuple's elements can be variables, not only literals. Moreover, they can be expressions if they're on the right side of the assignment operator.

# EXTRA: You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
my_tuple = tuple((1, 2, "string"))
print(my_tuple) #(1, 2, 'string')
my_list = [2, 4, 6]
print(my_list) # outputs: [2, 4, 6]
print(type(my_list)) # outputs: <class 'list'>
tup = tuple(my_list)
print(tup) # outputs: (2, 4, 6)
print(type(tup)) # outputs: <class 'tuple'>
# By the same fashion, when you want to convert an iterable to a list, you can use a Python built-in function called list():
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # outputs: <class 'list'>


### 4.6.3 Dictionaries
# The dictionary is another Python data structure. It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.

## How to make a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
print(dictionary) #{'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
print(phone_numbers) #{'Suzy': 5557654321, 'boss': 5551234567}
print(empty_dictionary) #{}
# In Python's world, the word you look for is named a key. The word you get from the dictionary is called a value.
# This means that a dictionary is a set of key-value pairs. Note:
    # each key must be unique − it's not possible to have more than one key of the same value;
    # a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
    # a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
    # the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
    # a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.
# First of all, it's a confirmation that dictionaries are not lists - they don't preserve the order of their data, as the order is completely meaningless (unlike in real, paper dictionaries). The order in which a dictionary stores its data is completely out of your control, and your expectations. That's normal. (*)
#   Note  
# (*) In Python 3.6x dictionaries have become ordered collections by default. Your results may vary depending on what Python version you're using.

# You mustn't use a non-existent key. Trying something like this:
print(phone_numbers['president'])
# will cause a runtime error. But, the in operator, together with its companion, not in, can salvage this situation:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

### 4.6.4 Dictionary methods and functions
## The keys() method
# Can dictionaries be browsed using the for loop, like lists or tuples? => # No and yes.
    # No, because a dictionary is not a sequence type − the for loop is useless with it.
    # Yes, because there are simple and very effective tools that can adapt any dictionary to the for loop requirements (in other words, building an intermediate link between the dictionary and a temporary sequence entity).
# The first of them is a method named keys(), possessed by each dictionary. The method returns an iterable object consisting of all the keys gathered within the dictionary. Having a group of keys enables you to access the whole dictionary in an easy and handy way:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])
# horse -> cheval
# dog -> chien
# cat -> chat

# Let's now have a look at a dictionary method called items(). The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
    print(english, "->", french)
# cat -> chat
# dog -> chien
# horse -> cheval

pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)

## Modifying and adding values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['cat'] = 'minou'
print(dictionary) #{'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}
# --------------------
for key in sorted(dictionary.keys()): #for sorting dictionaries
    print(key)
# There is also a method called values(), which works similarly to keys(), but returns values:
for french in dictionary.values():
    print(french) #As the dictionary is not able to automatically find a key for a given value, the role of this method is rather limited.

# Adding a new key-value pair to a dictionary is as simple as changing a value – you only have to assign a value to a new, previously non-existent key.
# Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.
dictionary['swan'] = 'cygne'
print(dictionary) #{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}
# Note: You can also insert an item to a dictionary by using the update() method, e.g.:
dictionary.update({"duck": "canard"})
print(dictionary)

## Removing a key
# Can you guess how to remove a key from a dictionary?
# Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys:
del dictionary['dog']
print(dictionary) #{'cat': 'chat', 'horse': 'cheval'}
#  EXTRA:  To remove the last item in a dictionary, you can use the popitem() method:
dictionary.popitem()
print(dictionary) # outputs: {'cat': 'chat', 'dog': 'chien'}
# ***In the older versions of Python, i.e., before 3.6.7, the popitem() method removes a random item from a dictionary.

# If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }
item_1 = pol_eng_dictionary["gleba"] # ex. 1
print(item_1) # outputs: soil
item_2 = pol_eng_dictionary.get("woda") # ex. 2
print(item_2) # outputs: water

# You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
print(len(pol_eng_dictionary)) # outputs: 3
del pol_eng_dictionary["zamek"] # remove an item
print(len(pol_eng_dictionary)) # outputs: 2
pol_eng_dictionary.clear() # removes all the items
print(len(pol_eng_dictionary)) # outputs: 0
del pol_eng_dictionary # removes the dictionary
