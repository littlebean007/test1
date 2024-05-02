from math import trunc
from parsers import parse 
import random

while True:
# Ask the user to enter a lower and an upper bound divided by a comma
  user_input = input(f"Enter a lower bound and an upper bound " \
                     f"divided a comma (e.g., 2,10): ")

# Parse the user string by calling the parse function
  try:
    parsed = parse(user_input)
  
    print(parsed)
    print(type(parsed))
  
  # Pick a random int between the two numbers
    rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
    print(rand)
    
    break
  
  except ValueError:
   print("Not a valid format! Please enter again")

print("bye")


# import playground
# import random


# lower_bound = int(input("Please enter a lower boundary number:"))
# upper_bound = int(input("Please enter an upper boundary number:"))

# # print(f"generated number: {random.randrange(lower_bound, upper_bound)}")

# print("generated number: - {}".
#        format(random.randrange(lower_bound, upper_bound)))



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("hi this is a list of numbers")
# print(a)
# print("this is #" + str(a[0]))

# print(len(a))
# j = 1
# for i in range(len(a)):
#   print("i:", i)
#   print("j:", j - 1)
#   j = j + 1

#   # print(i, a[i])
#   # print(j, a[j])


# print(type(a))
# print(a[0])

# #r_name=input("enter a name: ")
# #print(r_name)
# playground.display()
