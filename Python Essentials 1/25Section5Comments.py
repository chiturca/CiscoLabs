### 2.5.1 Comments – why, when, and how?
# A remark inserted into the program, which is omitted at runtime, is called a comment.
#Example:
# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of a square root.
print("c =", c)
# Good, responsible developers describe each important piece of code, for example, by explaining the role of the variables. Although it must be stated that the best way of commenting variables is to name them in an unambiguous manner.
# For example, if a particular variable is designed to store an area of some unique square, the name square_area will obviously be better than aunt_jane.
# We say that the first name is *self-commenting*.

### 2.5.2 Marking fragments of code
#You can use them to mark a piece of code that currently isn't needed for whatever reason. Look at the example below, if you uncomment the highlighted line, this will affect the output of the code:
x = 1
y = 2
# y = y + x
print(x + y)

#Comments can be important when you are reading your own code after some time (trust us, developers do forget what their own code does), and when others are reading your code (they can help them understand what your programs do and how they do it more quickly).
