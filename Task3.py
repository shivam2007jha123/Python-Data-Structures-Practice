s={1,2,3,4,5,6,7,8,9,10}
print(s)
# Removing duplicate values
s.add(1) # explains that we are adding a duplicate value to the set, which will not be added
print(s)
# Adding and removing elements
s.add(11)  # explains that we are adding the element 11 to the set s using the add() method
print(s)
#removing elements
s.remove(10) # explains that we are removing the element 10 from the set s using the remove() method
print(s)
s.union({12,13,14})  # explains that we are performing the union operation on the set s with another set {12,13,14}
print(s)
s.intersection({1,2,3,4,5})  # explains that we are performing the intersection operation on the set s with another set {1,2,3,4,5}
print(s)
s.difference({1,2,3,4,5})  # explains that we are performing the difference operation on the set s with another set {1,2,3,4,5}
print(s)