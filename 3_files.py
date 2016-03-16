# Let's learn about how to read data from files on disk.

# First, let's talk a bit about strings and escape characters.


# # Example of one way to read from a file
# file = open("landmarks.txt")
# lines = file.readlines()
# # readlines() is defined in "open"
# for name in lines:
#   print("****", name, "****")



# # CHALLENGE: How many landmarks are there?
# counter = 0
# for name in lines:
#   counter = counter + 1

# print(counter)




# CHALLENGE: Find the average of the numbers in numbers.txt.

with open('numbers.txt') as file:
  lines = file.read().splitlines()

  count = 0
  total = 0
  for num in range(len(lines)):
    count = count + 1
    total = total + int(lines[num])
  average = total/count


print(lines)
print(count)
print(total)
print(average)