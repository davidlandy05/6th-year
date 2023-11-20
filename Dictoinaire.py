1.
"""
sentence=input("Enter a sentence:")
chars={}
for char in sentence:
    if char in chars:
        chars[char]=chars[char]+1
    else:
        chars[char]=1
print(chars)
#counts how many times a letter appears in a word
"""
2.
sentence=input("Enter a sentence:")
chars={}
for char in sentence:
    print(char)    
    if char in chars:
        chars[char]=chars[char]+1
    else:
        chars[char]=1
print(chars)
#Seperates each letter of word