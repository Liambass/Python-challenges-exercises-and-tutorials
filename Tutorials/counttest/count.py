# We are going to write a Python program and write the tests for the program.

# Create 2 new python files within the same directory. Call one count.py and the other test_count.py.

# In count.py enter the following.

# def count(sequence, item):
#   sum = 0
#   for n in sequence:
#     if n == item:
#       sum += 1
#   return sum
# We are going to write 2 tests for this function. We are gonna test if the function works for integers as well as strings.

# Enter the following into test_count.py

# import count

# def test_count_zeros():
#     assert count.count([0,0,0], 0) == 3

# def test_count_string():
#     assert count.count(["a","a","a"], "a") == 3
# The count which we import is the file count.py, so we have to specify which function from count.py we wish to use.
# This is done by using count.count().

# Now run the command:

# python3 -m pytest
# You should be able to see the tests have passed.

def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum