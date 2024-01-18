# Day 13 - 100 Days of Code - The Complete Python Pro Bootcamp for 2023
# Project: Debugging

# The objetive of this day is to learn how to debug a code, using the print() function and the debugger.


"""
Code with the bug:

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])


"""

# Solution:
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: # use and (not or)
    print("FizzBuzz")
  elif number % 3 == 0: # use elif (not if)
    print("Fizz")
  elif number % 5 == 0: # use elif (not if)
    print("Buzz")
  else:
    print(number) # remove square brackets []