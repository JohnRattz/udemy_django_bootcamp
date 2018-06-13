#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    sublist = [1,2,3]
    n = len(sublist)
    return any((sublist == nums[i:i+n]) for i in range(len(nums)-n+1))

print(arrayCheck([1, 1, 2, 3, 1])) # True
print(arrayCheck([1, 1, 2, 4, 1])) # False
print(arrayCheck([1, 1, 2, 1, 2, 3])) # True

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  return(str[::2])

print(stringBits('Hello')) # 'Hlo'
print(stringBits('Hi')) # 'H'
print(stringBits('Heeololeo')) # 'Hello'

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    a = a.lower(); b = b.lower()
    return a.endswith(b) or b.endswith(a)
    # return (a in b) or (b in a)

print(end_other('Hiabc', 'abc')) # True
print(end_other('AbC', 'HiaBc')) # True
print(end_other('abc', 'abXabc')) # True

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    return ''.join(char*2 for char in str)

print(doubleChar('The')) # 'TThhee'
print(doubleChar('AAbb')) # 'AAAAbbbb'
print(doubleChar('Hi-There')) # 'HHii--TThheerree'

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    def fix_teen(n):
        return 0 if (n in set(range(13,20)) - set(range(15,17))) else n
    return sum(map(fix_teen, [a,b,c]))

print(no_teen_sum(1, 2, 3)) # 6
print(no_teen_sum(2, 13, 1)) # 3
print(no_teen_sum(2, 1, 14)) # 3


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    count = 0
    for num in nums:
        if num%2==0:
            count += 1
    return count

print(count_evens([2, 1, 2, 3, 4])) # 3
print(count_evens([2, 2, 0])) # 3
print(count_evens([1, 3, 5])) # 0
