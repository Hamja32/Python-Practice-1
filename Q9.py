#9 Write a python program to find the repeated items in a tuple

def find_repeated_items(t):
    repeated_items = []
    for item in t:
        if t.count(item) > 1 and item not in repeated_items:
            t.count(item)
            repeated_items.append(item)
    return repeated_items

t = (1,2,3,4,3,2,5)
print("Repeated items : ",find_repeated_items(t))
