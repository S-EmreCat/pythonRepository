# https://pynative.com/python-set-exercise-with-solutions/

# Exercise 1: Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

res = sample_set.union(sample_list)
sample_set.update(sample_list)
# print(sample_set)

# Exercise 2: Return a new set of identical items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

res = set1.intersection(set2)

# Exercise 3: Get Only unique items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

res= set1.union(set2)

# Exercise 4: Update the first set with items that don’t exist in the second set

set1 = {10, 20, 30}
set2 = {20, 40, 50}
res = set1.difference(set2)


# Exercise 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
set1.remove(10)
set1.discard(20)
# print(set1)

# Exercise 6: Return a set of elements present in Set A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

res = set1.symmetric_difference(set2)

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

res = set1.isdisjoint(set2)
# if set1.isdisjoint(set2):
#   print("Two sets have no items in common")
# else:
#   print("Two sets have items in common")
#   print(set1.intersection(set2))


# Exercise 8: Update set1 by adding items from set2, except common items
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
res = set1.symmetric_difference(set2)

# Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
res = set1.intersection(set2)



print(res)