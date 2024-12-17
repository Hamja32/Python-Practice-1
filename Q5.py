#Q5 Write a python script to sort (ascending and descending) a dictionary by value
dict1 = {'a':4,'b':3,'c':8}

ascending = dict(sorted(dict1.items(), key=lambda item:item[1]))
print(ascending)

descending = dict(sorted(dict1.items(), key=lambda item:item[1],reverse=True))
print(descending)



