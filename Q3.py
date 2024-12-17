#3 Write a python program to get the difference between the two lists

a = [1,2,3,4,5]
b = [4,5,6,7,8]
difference = list(set(a) - set(b))
print("Difference : ",difference)
