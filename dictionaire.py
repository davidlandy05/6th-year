
#1 The code ask for a sentence and thern check if the word in char is in the sentence
#it adds one to value else it value becomes 1

#2
sentence =input("input a sentence")
vowel={"a","i","o","u","e"}
constance={ "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P"," Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}
chars={}
for char in vowel:
    for char2 in sentence:
        if char==char2:
             chars[char]=chars.get(char,0)+1
        vowels=char2+char
print(vowel)
#3 stores chracter data in a fixed-leenght field.
"""
4.
the char keys are letters in the word
the chars values are how many times each letter appears
"""
#6
#The get dictiomary operation gets the char value so if it ddoesnt exist it makes it added 1
#If it does exist it will add one to the existing char value
#7
