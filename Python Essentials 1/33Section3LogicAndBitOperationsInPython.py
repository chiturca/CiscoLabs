### 3.3.1 Computer logic
    # If we have some free time, *and* the weather is good, we will go for a walk.
# We've used the conjunction and, which means that going for a walk depends on the simultaneous fulfilment of these two conditions. In the language of logic, such a connection of conditions is called a *conjunction*. And now another example:
    # If you are in the mall *or* I am in the mall, one of us will buy a gift for Mom.
# The appearance of the word or means that the purchase depends on at least one of these conditions. In logic, such a compound is called a *disjunction*.
# It's clear that Python must have operators to build conjunctions and disjunctions. Without them, the expressive power of the language would be substantially weakened. They're called logical operators.

## The and operator
#counter > 0 and value == 100
# Argument A	Argument B	    A and B
# False	        False	        False
# False	        True	        False
# True	        False	        False
# True	        True	        True

## The or operator
# Argument A	Argument B	    A or B
# False	        False	        False
# False	        True	        True
# True	        False	        True
# True	        True	        True

## The not operator  #*unary* operator performing a logical negation. Its operation is simple: it turns truth into falsehood and falsehood into truth.
# Argument	not Argument
# False	    True
# True	    False

### 3.3.2 Logical expressions
# You may be familiar with De Morgan's laws. They say that:
    # The negation of a conjunction is the disjunction of the negations.
    # The negation of a disjunction is the conjunction of the negations.
# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q) 
# none of these two-argument operators can be used in the abbreviated form known as *op=*.

### 3.3.3 Logical values vs. single bits
# The operators are aware only of the value: zero (when all the bits are reset) means False; not zero (when at least one bit is set) means True.

### 3.3.4 Bitwise operators
# there are four operators that allow you to manipulate single bits of data. They are called bitwise operators. They cover all the operations we mentioned before in the logical context, and one additional operator. This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).
    # & (ampersand) ‒ bitwise conjunction;
    # | (bar) ‒ bitwise disjunction;
    # ~ (tilde) ‒ bitwise negation;
    # ^ (caret) ‒ bitwise exclusive or (xor).
# Argument A	Argument B	A & B	 A | B	  A ^ B
# 0	            0	        0	     0	      0
# 0	            1	        0	     1	      1
# 1	            0	        0	     1	      1
# 1	            1	        1	     1	      0 ##But, like, how??
    # & requires exactly two 1s to provide 1 as the result;
    # | requires at least one 1 to provide 1 as the result;
    # ^ requires exactly one 1 to provide 1 as the result***.
# The difference in the operation of the logical and bit operators is important: the logical operators do not penetrate into the bit level of its argument. They're only interested in the final integer value.
# Bitwise operators are stricter: they deal with every bit separately. If we assume that the integer variable occupies 64 bits (which is common in modern computer systems), you can imagine the bitwise operation as a 64-fold evaluation of the logical operator for each pair of bits of the arguments. This analogy is obviously imperfect, as in the real world all these 64 operations are performed at the same time (simultaneously).

## Logical vs. bit operations
# i = 15    32Bit:  i: 00000000000000000000000000001111
# j = 22    32Bit:  j: 00000000000000000000000000010110
# log = i and j => True

# bit = i & j =>
# i	            00000000000000000000000000001111
# j	            00000000000000000000000000010110
# bit = i & j	00000000000000000000000000000110  ==> integer value of six.

### 3.3.5 How do we deal with single bits?
# Imagine that you're a developer obliged to write an important piece of an operating system. You've been told that you're allowed to use a variable assigned in the following way:
    # flag_register = 0x1234
# The variable stores the information about various aspects of system operation. Each bit of the variable stores one yes/no value. You've also been told that only one of these bits is yours ‒ the third (remember that bits are numbered from zero, and bit number zero is the lowest one, while the highest is number 31). The remaining bits are not allowed to change, because they're intended to store other data. Here's your bit marked with the letter x:
    # flag_register = 0000000000000000000000000000x000
## 1. Check the state of your bit ‒ you want to find out the value of your bit; comparing the whole variable to zero will not do anything, because the remaining bits can have completely unpredictable values, but you can use the following conjunction property:
    # x & 1 = x
    # x & 0 = 0
# If you apply the & operation to the flag_register variable along with the following bit image:
    # 00000000000000000000000000001000
# (note the 1 at your bit's position) as the result, you obtain one of the following bit strings:
    # 00000000000000000000000000001000 if your bit was set to 1
    # 00000000000000000000000000000000 if your bit was reset to 0

# Such a sequence of zeros and ones, whose task is to grab the value or to change the selected bits, is called a bit mask.
# Let's build a bit mask to detect the state of your bit. It should point to the third bit. That bit has the weight of 23 = 8. A suitable mask could be created by the following declaration:
    # the_mask = 8
# You can also make a sequence of instructions depending on the state of your bit. Here it is:
    # if flag_register & the_mask:
    #     # My bit is set.
    # else:
    #     # My bit is reset.

## 2. Reset your bit ‒ you assign a zero to the bit while all the other bits must remain unchanged; let's use the same property of the conjunction as before, but let's use a slightly different mask ‒ exactly as below:
    # 11111111111111111111111111110111
# Resetting the bit:
    # flag_register = flag_register & ~the_mask
    # flag_register &= ~the_mask

## 3. Set your bit ‒ you assign a 1 to your bit, while all the remaining bits must remain unchanged; use the following disjunction property:
    # x | 1 = 1
    # x | 0 = x
# You're now ready to set your bit with one of the following instructions:
    # flag_register = flag_register | the_mask
    # flag_register |= the_mask

## 4. Negate your bit ‒ you replace a 1 with a 0 and a 0 with a 1. You can use an interesting property of the xor operator:
    # x ^ 1 = ~x
    # x ^ 0 = x
# and negate your bit with the following instructions:
    # flag_register = flag_register ^ the_mask
    # flag_register ^= the_mask

### 3.3.6 Binary left shift and binary right shift
# shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).
# The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.
    # value << bits
    # value >> bits
# The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.
# It shows that this operation is certainly not commutative.
var = 17
var_left = var << 2
var_right = var >> 1
print(var, var_left, var_right) #17 68 8
# Note:
    # 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)
    # 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
# And here is the updated priority table, containing all the operators introduced so far:
# Priority	Operator	
# 1	        ~, +, -	unary
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	binary
# 5	        <<, >>	
# 6	        <, <=, >, >=	
# 7	        ==, !=	
# 8	        &	
# 9	        |	
# 10	    =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

# * -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.=>https://en.wikipedia.org/wiki/Two%27s_complement