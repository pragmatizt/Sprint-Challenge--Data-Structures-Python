import time
from binary_search import BinarySearchTree
"""
original runtime complexity on my laptop:
runtime: 13.456114292144775 seconds
"""

# Initialize the binary tree:
bst = BinarySearchTree("dupes")    # Looks like we need a value inside () here

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
0:29:00 mark from Thursday's lecture: https://youtu.be/_2gJLjhquXE
In BST, "contains" returns TRUE if the tree contains the value.  So it will run 
"""


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""
Since we're dealing with dupes, let's set names_1 as our base case
We add elements of list names_1 to the BST
Then compare all elements of the list to name_2
----
For the longest time I was trying to figure out, "how do I pass the first list,
then have the tree remember and compare that against the second list?

We pass it once on name_1 and the tree will contain the name;
then we run "contains" on it -- and we do an if statement
if bst.contains name_2, append that to the duplicates list.
"""
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:  # running python names.py timed out until I shifted this to left
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# HOLY SMOKES.  runtime: 0.179640531539917 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
