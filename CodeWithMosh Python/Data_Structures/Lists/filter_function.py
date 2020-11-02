items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = filter(lambda item: item[1] >= 10, items)
print(filtered)
# list comprehension
filtered = [item[1] for item in items if item >= 10]
