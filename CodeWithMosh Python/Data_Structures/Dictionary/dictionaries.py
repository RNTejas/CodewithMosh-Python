point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10         # changing the value of x from 1 to 10
point["z"] = 20         # adding another key to dictionary 'z'

# print(point["a"])       # 'a' is not in the dict gives an error
# to avoid the error use for loop r use .get function
print(point.get("a", 0))    # 0 is a default value if a is not in the dict
# to delete an key in the dict we use 'del' function
del point["x"]
print(point) 
# looping over the dictionary
# for key in point:
#     print(key, point[key])
# another way 
for key, value in point.items():
    print(key, value)
    