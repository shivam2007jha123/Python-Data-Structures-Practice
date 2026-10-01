n=(1,2,3,4,5,6,7,8,9,10)
print(n)
# Accessing elements using indexing
print(n[2])  # explains that we are accessing the element at index 2 (the third element)    
print(n[0])  # explains that we are accessing the element at index 0 (the first element)
# Tuple slicing 
print(n[2:5])  # explains that we are slicing the tuple from index 2 to index 5 (not including index 5)
print(n[:5])  # explains that we are slicing the tuple from the beginning to index 5
print(n[0:]) # explains that we are slicing the tuple from index 0 to the end

# tuple operations
print(len(n))  # explains that we are finding the length of the tuple using the len() function
# explains that we are performing basic tuple operations such as concatenation and repetition
n1=(11,12,13)
n2=n+n1  # concatenation
print(n2)
n3=n*2  # repetition
print(n3)
