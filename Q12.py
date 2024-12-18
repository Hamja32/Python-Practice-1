# 12 Write a python program to append text to a file and display the text
print("File Before append : \n")
f = open('sample.txt','r')
text = f.read()
print(text,'\n')
f.close()

f = open('sample.txt','a')
f.write('\nIt is the most easy language')
f.close()

print("File After Append\n")
f = open('sample.txt','r')
output = f.read()
print(output)
f.close()




