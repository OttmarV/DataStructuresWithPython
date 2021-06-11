"""
No duplicates
No indexing
whole set is mutable
Unordered when looping

A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.


Basically, sets are used for membership testing and eliminating duplicate entries.

Sets are an unordered collection of unique values.
A single set contains values of any immutable data type.
"""

# Creating a set
# Accessing Values in a Set

days={92,74,102,55,0}
times=set([12,34,55,0,10])
#print(type(times))
#print(type(days))
print(times)

for element in days:
    print(element)

times=set([1,2,3,4,5])

# Adding Items to a Set
times.add(10)
times.add(100)
print(times)

"""
Both the discard() and remove() functions take a single value as an argument and 
removes that value from the set. If that value is not present, discard() does nothing, 
but remove() will raise a KeyError exception.
"""

# Removing Item from a Set
times.discard(5)
times.discard(3)
print(times)

# Union of Sets(|)
timer=set([10,2,30,73])
print(timer)
print(times|timer)

# Intersection of Sets(&)
print(times&timer)

# Compare Sets(<=)
print( times <= timer) #timer no es un superset de times





