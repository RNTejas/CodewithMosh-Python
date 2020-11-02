items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
items.sort(key=lambda items: items[1])
print(items)
# if you want to sort the list of tuples using the sort method you should define a function but there
# is always better way of doing anythng 
# here in the above code we have used the lambda function
 
