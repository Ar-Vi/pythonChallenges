#WORD FRAMES
#Arya Vishnu
#Framing words

word = " " + input("Give word: ")
starAmnt = "* "*len(word)

#print("*", end = "")
#for i in word:
 #   print(i, end = " ")
#print("*", end = "")

print("*", end = " ")
for i in range(1, len(word)):
    print(word[i::-i], end = "")
print("*")

for i in range(1, len(word)):
    print(word[i] + starAmnt + word[-i])
    

print("*", end = " ")
for i in range(1, len(word)):
    print(word[-i::i], end = " ")
print("*", end = "")
