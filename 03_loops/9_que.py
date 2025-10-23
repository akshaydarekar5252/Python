items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()  #--> it stores only unique values 

for item in items:
    if item in unique_item:
        print("dublicate item is :",item)
        break
    unique_item.add(item)