list1 = [8, 8, 12, 12, 8]
list2 = [8, 8, 8, 12, 12]
list3 = [1, 8, 8, 12, 12]
 
print("Compare List1 and List2 : ",''.join(map(str, list2)) in ''.join(map(str, list1 *2)))
print("Compare List1 and List3 : ",' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

# print(' '.join(map(str, list1*2)))
# print(list1 + list1)
print((map(str, list2)) in (map(str, list1 * 2)))

print(" ".join((map(str, list2))))
print(' '.join(map(str, list1 *2)))

# combined_tuple
tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

