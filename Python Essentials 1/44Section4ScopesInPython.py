### 4.4.2 Functions and scopes: the global keyword
# There's a special Python method which can extend a variable's scope in a way which includes the function's body (even if you want not only to read the values, but also to modify them).
# Such an effect is caused by a keyword named global:
    # global name
    # global name1, name2, ...
# Using this keyword inside a function with the name (or names separated with commas) of a variable (or variables), forces Python to refrain from creating a new variable inside the function ‒ the one accessible from outside will be used instead.
# In other words, this name becomes global (it has global scope, and it doesn't matter whether it's the subject of read or assign).
a = 1
def fun():
    global a
    a = 2
    print(a)
fun()
a = 3
print(a)
# 2
# 3

# ----------------#
a = 1
def fun():
    global a
    a = 2
    print(a)
a = 3
fun()
print(a)
# 2
# 2