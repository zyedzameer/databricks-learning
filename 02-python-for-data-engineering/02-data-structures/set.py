numset = {}  # this creates an empty dictionary
print(type(numset))

numset = set()  # this creates an empty set
print(type(numset))

print("************* set created with duplicate values, dupes will be removed")
numset = {10, 24, 36, 40, 24, 10, 57, 60, 70, 36}
print(numset)

# sets are unordered and do not support indexing
# numset[0] # will raise error - TypeError : 'set' object is not subscrptable

numset.add(110)  # adding element to the set

print("*********** iterating over the set")
for i in numset:
    print(i)

# update() accepts any iterable and adds its element to the set
numset.update([1, 2, 3, 4])
print("************after udpate")
print(numset)

# pop() removes and returns an arbitrary element (since sets are unordered)
removed = numset.pop()
print(removed)

# remove() deletes specified element; raises KeyError if not present
numset.remove(24)

# discard() deletes specefied element; does nothing if element not found
numset.discard(44)

# use set to remove dups from given list
list_with_dups = [1, 2, 4, 6, 3, 6, 2, 2, 1]
dupes_removed = list(set(list_with_dups))
print(dupes_removed)

# set supports operations like union,intersection,difference,symmetric_difference