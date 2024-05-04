### 2.2.1 Literals – the data in itself
# print("2")
# print(2)

# clue: 2 is a literal, and c is not (but "c" or "2" is a string literal).
# You use literals to encode data and to put them into your code. 

###2.2.2 Integers
# integers, that is, those which are devoid of the fractional part;
# and floating-point numbers (or simply floats), that contain (or are able to contain) the fractional part.

# 11,111,111, or like this: 11.111.111, or even like this: 11 111 111.
# It's clear that this provision makes it easier to read, especially when the number consists of many digits. However, Python doesn't accept things like these. It's prohibited. What Python does allow, though, is the use of underscores in numeric literals.*
# Therefore, you can write this number either like this: 11111111, or like this: 11_111_111.

## Octal and hexadecimal numbers
# If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
# 0o123 is an octal number with a (decimal) value equal to 83.
print(0o123)
# The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).
# 0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. Try this:
print(0x123)

###2.2.3 Floats
# Whenever we use a term like two and a half or minus zero point four, we think of numbers which the computer considers floating-point numbers:
# 2.5 -0.4
#  You can omit zero when it is the only digit in front of or after the decimal point.
# In essence, you can write the value 0.4 as:
# .4
# For example: the value of 4.0 could be written as:
# 4.

##Ints vs. floats
# 4 is an integer number, whereas 4.0 is a floating-point number.(Not same type)

# On the other hand, it's not only points that make a float. You can also use the letter e.
# When you want to use any numbers that are very large or very small, you can use scientific notation.
# Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000.
# To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.
# It reads: three times ten to the power of eight.
# In Python, the same effect is achieved in a slightly different way ‒ take a look:
# 3E8
# The letter E (you can also use the lower-case letter e ‒ it comes from the word exponent) is a concise record of the phrase times ten to the power of.
# the exponent (the value after the E) has to be an integer;
# the base (the value in front of the E) may be either an integer or a float.

# A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.
# If you would like to use it in a program, you should write it this way:
# 6.62607E-34
print(0.0000000000000000000001)
# 1e-22

###2.2.4 Strings
# I like "Monty Python"
print("I like \"Monty Python\"")
print('I like "Monty Python"')
print('I\'m Monty Python.')
print("I'm Monty Python.")

###2.2.5 Boolean values
# The name comes from George Boole (1815-1864), the author of the fundamental work, The Laws of Thought, which contains the definition of Boolean algebra ‒ a part of algebra which makes use of only two distinct values: True and False, denoted as 1 and 0.
print(True > False) 
print(True < False)
#True==1 False==0
# String example:
# Expected output: "I'm" ""learning"" """Python""" ==> print() in one line?
print('"I\'m" ""learning"" """Python"""')

# Extra  
# There is one more, special literal that is used in Python: the None literal. This literal is a NoneType object, and it is used to represent the absence of a value. We'll tell you more about it soon.

# Question: What is the decimal value of the following binary number?
# 1011
# It's 11, because (2**0) + (2**1) + (2**3) = 11
