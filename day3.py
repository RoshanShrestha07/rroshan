
# # takes a secret word as input (without spaces)
# then encodes the word using a custom cipher
# replace all the vowels with *
# reverse the entire String 
# then shift each letter 2 places ahead in the alphabet (wrap around if needed , eg , y-a, z-b)
# finally , print the result encoded



word = input("Enter a secret word: ")

vowels = "aeiouAEIOU"
no_vowels = ""
for letter in word:
    if letter in vowels:
        no_vowels += '*'
    else:
        no_vowels += letter

reversed_word = no_vowels[::-1]

encoded = ""
for letter in reversed_word:
    if letter.isalpha():
        if letter.islower():
            shifted = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
        else:
            shifted = chr((ord(letter) - ord('A') + 2) % 26 + ord('A'))
        encoded += shifted
    else:
        encoded += letter

print("Encoded word:", encoded)





L1 = [1,8,7,2,21,15]
L1.sort()
print(L1)

L1.reverse()
print(L1)

L1.append(9)
print(L1)

L1.insert(3,8)
print(L1)

L1.pop(5)
print(L1)


L1.remove(7)
print(L1)


# write a program to store 7 fruits in a list entered by the user 
# fruits = []
# for i in range(7):
#     fruit = input("Enter a fruit: ")
#     fruits.append(fruit)
# print("Fruits list:", fruits)

# wap to accept marks of 6 student and display in list
marks = []  
for i in range(6):
    mark = int(input("Enter marks for student {}: ".format(i + 1)))
    marks.append(mark)
print("Marks list:", marks) 

# write a progress to sum a list with 4 numbers 
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("The sum is:", total)


# # tuple 
# tuple is a immutable data type in python which is enclosed within parenthesis which can have any data types in it.
# example of tuple
# a = (1,5,3,5)
# types of tuple:
# 1.empty tuple represented as : tuple1= ()
# 2.single data type represented as single = (1,)
# 3.normal tuple represented as normal = (1,6,8,5,,10)
 
