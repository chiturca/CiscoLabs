###2.3.1 Python as a calculator
print(2+2) #4

###2.3.2 Basic operators
#An operator is a symbol of the programming language, which is able to operate on the values.
#+ - * / // % **
#Remember: Data and operators when connected together form expressions. The simplest expression is a literal itself.

##Exponentiation
print(2 ** 3) #8
print(2 ** 3.) #8.0
print(2. ** 3) #8.0
print(2. ** 3.) #8.0
##Multiplication
print(2 * 3) #6
print(2 * 3.) #6.0
print(2. * 3) #6.0
print(2. * 3.) #6.0
#Division
print(6 / 3) #2.0
print(6 / 3.) #2.0
print(6. / 3) #2.0
print(6. / 3.) #2.0
#Integer division (floor division)
print(6 // 3) #2
print(6 // 3.) #2.0
print(6. // 3) #2.0
print(6. // 3.) #2.0
print(6 // 4) #1
print(6. // 4) #1.0
print(-6 // 4) #-2
print(6. // -4) #-2.0
#Remainder (modulo)
print(14 % 4) #2
print(12 % 4.5) #3.0

###2.3.3 Operators and their priorities
#2 + 3 * 5
#The phenomenon that causes some operators to act before others is known as the hierarchy of priorities.
#Python precisely defines the priorities of all operators, and assumes that operators of a higher priority perform their operations before the operators of a lower priority.
 
##Operators and their bindings
#Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.
print(9 % 6 % 2) #1
print(2 ** 2 ** 3) #256 ==> the exponentiation operator uses right-sided binding. ==> 2 ** 3 → 8; 2 ** 8 → 256
print(-3 ** 2) #-9
print(-2 ** 3) #-8
print(-(3 ** 2)) #-9

# Priority	Operator	
# 1	        **	
# 2	        +, - unary(note: unary operators located next to the right of the power operator bind more strongly)	
# 3	        *, /, //, %	
# 4	        +, -	binary
print(2 * 3 % 5)

##Operators and parentheses
#In accordance with the arithmetic rules, subexpressions in parentheses are always calculated first
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) #10.0

print((2 ** 4), (2 * 4.), (2 * 4)) #16 8.0 8
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) #-0.5 0.5 0 -1
print((2 % -4), (2 % 4), (2 ** 3 ** 2)) #-2 2 512  ==> for gods' sake, what even is this???
# The output of print(2 ** 3 ** 2) being 512 might seem surprising at first, but it follows the rules of operator precedence in Python.
# In Python, the ** operator represents exponentiation and has right-to-left associativity, meaning the expression is evaluated from right to left.
# Let's break it down step by step:
# 3 ** 2: This evaluates to 9. It calculates 3 raised to the power of 2.
# 2 ** 9: This evaluates to 512. It calculates 2 raised to the power of 9.
# Therefore, the output of print(2 ** 3 ** 2) is 512.
