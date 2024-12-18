#13 Write a python program to read an entire file
def file_read(fname):
    text = open(fname)
    print(text.read())
        

file_read('sample.txt')