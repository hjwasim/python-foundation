# Count Letter occurances in string.
string = input("ENTER ANY STRING.... \n")
# input - AAAABBBCC
d = {}
for character in string:
    d[character] = d.get(character, 0) + 1

print(d)
# output - {'A': 4, 'B': 3, 'C': 2}

# Count vowel letters in string
string = input("ENTER ANY STRING.... \n")
# input - aeaemm
d = {}
vowels = {'a', 'e', 'i', 'o', 'u'}

for character in string:
    if character in vowels:
        d[character] = d.get(character, 0) + 1
print(d)
# output - {'a': 2, 'e': 2}