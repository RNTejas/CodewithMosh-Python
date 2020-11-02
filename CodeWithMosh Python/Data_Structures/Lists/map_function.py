items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# let's imagine you want to transform this list of 
# tuples into list of tuples of numbers only
# the basic way
prices = []
for item in items:
    prices.append(item[1])

print(prices)

# let's use map function  
x = list(map(lambda item: item[1], items))        # here we use items because we want to iterate over it for every time like for loop
# and the x returns another iterable so we have to iterate over it again
print(x)
for item in x:
    print(item)

# at last we use list function in the variable 'x' 

