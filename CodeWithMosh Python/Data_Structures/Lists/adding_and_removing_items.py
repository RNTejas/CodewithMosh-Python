# ADDING
# you can add or remove items in lists because they're mutable sequence types
# if you want to add a utem at the end of the list you can use .append method
letters = ["a", "b", "c"]
letters.append("d")
print(letters)
# if you want to add a item at the specific position you should use the .insert method letters.insert(0, "A")
letters.insert(0, "--")
print(letters)

# REMOVING
# if you want to remove an item from the end of the list you should use ".pop" method
letters.pop()           # it will remove the letter letter 'd'
                        # if you specify the index then it will remove the items from that index
print(letters)
# if you want to remove an item but don't know it's index position then use the .remove method
letters.remove("--")
print(letters)

# you can remove by another method del function
del letters[0:1]
print(letters)

# if you want to clear the list you can use the .clear method
letters.clear()
 