# Let's learn about how to read data from files on disk.

# First, let's talk a bit about strings and escape characters.


# Example of one way to read from a file
file = open("landmarks.txt")
lines = file.readlines()
for name in lines:
  print("****", name, "****")



# CHALLENGE: How many landmarks are there?




# CHALLENGE: Find the average of the numbers in numbers.txt.
