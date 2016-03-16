# Let's learn about functions, the DRY principle,
# function arguments/parameters, and scope.

# DEMO:


# def greeting():
#   for i in range(3):
#     name = input("What is your name? ")
#     print("Hello, ", name)
#     print("Nice to meet you.")

# greeting()





# 1. CHALLENGE: How would you write a function to help
#    simplify the following code?
#
# print("Chicago Landmarks")
# print("-----------------")
# print("Wrigley Field costs about $40 and is located at 1033 W. Addison St.")
# print("The Bean costs $0 and is located at Millenium Park.")
# print("The John Hancock Tower costs about $35 and is located at 1875 N. Michigan Ave.")
# print("The United Center costs about $75 and is located at 11901 W. Madison St.")
# print("The Shakespeare Theater costs about $40 and is located at 1Navy Pier")

# My solution
# def main():
#   landmark = input("What is the name of the landmark? ")
#   cost = input("How much does it cost? ")
#   location = input("Where is it located? ")
#   print(landmark, " costs about ", cost, " and is located at ", location)

# main()

# His solution
# def display(name, cost, address):
#   print(name, "costs about", cost, " and is located at ", address)

# display("Wrigley Field", "$40", "151 N Michigan")

def admission(number_of_people, cost):
  total_cost = number_of_people * cost
  return total_cost

x = admission(4, 20)
print(x)

# 2. Functions That Return a Value
