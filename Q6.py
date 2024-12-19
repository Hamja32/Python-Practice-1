#Q6 Write a python script to concatenate following dictionaries to create a new one
# dict1 = {1:10,2:20}
# dict2= {3:30,4:40}
# dict3 = {5:50,6:60}
#expected result {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}

result = {**dict1,**dict2,**dict3}
print("New Dictionary : ",result)