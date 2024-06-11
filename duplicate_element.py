list = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in list:
    if item in unique_item:
        print("the duplicate item is", item)
        break;
    unique_item.add(item)
