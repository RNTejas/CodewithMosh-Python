sentence = "This is the most common interview question"
char_friquency = {}
for char in sentence:
    if char in char_friquency:
        char_friquency[char] += 1
    else:
        char_friquency[char] = 1

char_friquency_sorted = sorted(
    char_friquency.items(),
    key=lambda kv: kv[1],
    reverse=True) 
print(char_friquency_sorted[1])
