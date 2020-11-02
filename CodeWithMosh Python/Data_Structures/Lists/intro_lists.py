# lists are really useful when creating real-world application 
# lists can contain all types of data such as Strings Integers Floats Booleans and Lists 

letters = ["a", "b", "c", "d"]
list_of_lists = [[1, 2], ["a", "b"], [3, 4], ["c", "d"]]
# list of 100 '0's
zeros = [0] * 5 # 100
combined = zeros + letters
print(combined)
# creating list of 20 numbers
twenty_numbers = list(range(1, 21))
print(twenty_numbers)
# list of chars
chars =  list("Hello World")
print(len(chars))
