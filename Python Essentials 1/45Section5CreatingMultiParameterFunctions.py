### 4.5.1 Sample functions: Evaluating the BMI
# Let's get started on a function to evaluate the Body Mass Index (BMI).
# As you can see, the formula gets two values:
    # weight (originally in kilograms)
    # height (originally in meters)
# It seems that this new function will have two parameters. Its name will be bmi, but if you prefer any other name, use it instead.
def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65)) #19.283746556473833

## Evaluating BMI and converting imperial units to metric units
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(352.5, 1.65)) #None
    # First, the test invocation ensures that the protection works properly ‒ the output is:None
    # Second, take a look at the way the backslash (\) symbol is used. If you use it in Python code and end a line with it, it will tell Python to continue the line of code in the next line of code.
# This function is not too useful for people accustomed to pounds, feet, and inches.
# We can write two simple functions to convert imperial units to metric ones. Let's start with pounds.
# *1 lb = 0.45359237 kg*
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1)) #0.45359237
# *feet and inches: 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m*
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1)) #0.3302
# It's quite possible that sometimes you may want to use just feet without inches. Will Python help you? Of course it will.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))

### 4.5.2 Sample functions: Triangles
# Let's play with triangles now. We'll start with a function to check whether three sides of given lengths can build a triangle.
# We know from school that the sum of two arbitrary sides has to be longer than the third side.
# It will return True if the sides can build a triangle, and False otherwise. In this case, is_a_triangle is a good name for such a function.
def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
# This is a more compact version:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
# Can we compact it even more? Yes, we can - look:
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 1, 1)) #True
print(is_a_triangle(1, 1, 3)) #False
# We've negated the condition (reversed the relational operators and replaced ors with ands, receiving a universal expression for testing triangles).

## Triangles and the Pythagorean theorem
# In the second step, we'll try to ensure that a certain triangle is a right-angle triangle.
# We will need to make use of the Pythagorean theorem:
    # c2 = a2 + b2
# The hypotenuse is the longest side.
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4)) #True
print(is_a_right_triangle(1, 3, 4)) #False

## Evaluating a triangle's area
# We can also evaluate a triangle's area. *Heron's formula* will be handy here:
# s = (a+b+c)/2     A = (s(s-a)(s-b)(s-c))**0.5
# We're going use the exponentiation operator to find the square root ‒ it may seem strange, but it works:
# x = x**1/2
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
print(area_of_triangle(1., 1., 2. ** .5)) #0.49999999999999983
# It's very close to 0.5, but it isn't exactly 0.5. What does it mean? Is it an error?
# No, it isn't. This is the specifics of floating-point calculations. We'll tell you more about it soon.

# 4.5.3 Sample functions: Factorials
# Another function we're about to write is factorials. Do you remember how a factorial is defined?
# 0! = 1 (yes! it's true)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 * 3 * 4 * ... * n-1 * n
# It's marked with an exclamation mark, and is equal to the product of all natural numbers from one up to its argument.
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
for n in range(1, 6): # testing
    print(n, factorial_function(n))

# 4.5.4 Fibonacci numbers
# They are a sequence of integer numbers built using a very simple rule:
    # the first element of the sequence is equal to one (Fib1 = 1)
    # the second is also equal to one (Fib2 = 1)
    # every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)
# Here are some of the first Fibonacci numbers:
# fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
for n in range(1, 10): # testing
    print(n, "->", fib(n))
# Analyze the for loop body carefully, and find out how we move the elem_1 and elem_2 variables through the subsequent Fibonacci numbers.

### 4.5.5 Recursion
# This term may describe many different concepts, but one of them is especially interesting − the one referring to computer programming.
# In this field, recursion is a technique where a function invokes itself.
    # These two cases seem to be the best to illustrate the phenomenon − factorials and Fibonacci numbers. Especially the latter.
# The Fibonacci numbers definition is a clear example of recursion. We already told you that:
    # Fib(i) = Fib(i-1) + Fib(i-2)
# The definition of the ith number refers to the i-1 number, and so on, till you reach the first two.
# Can it be used in the code? Yes, it can. It can also make the code shorter and clearer:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
# ***There is a little risk indeed. If you forget to consider the conditions which can stop the chain of recursive invocations, the program may enter an infinite loop. You have to be careful.
# ***You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.

# The factorial has a second, recursive side too. Look:
    # n! = 1 × 2 × 3 × ... × n-1 × n
# It's obvious that:
    # 1 × 2 × 3 × ... × n-1 = (n-1)!
# So, finally, the result is:
    # n! = (n-1)! × n
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1  # The base cases (termination conditions.)
    return n * factorial_function(n - 1)   
for n in range(1, 6): # testing
    print(n, factorial_function(n))

# ------------------------------- #
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25)) #56