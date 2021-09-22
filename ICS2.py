#ALPHABETICAL
#Arya Vishnu
#In case you forget what order the alphabet is in 


rep = True


while rep == True:
    word1 = input("-----------\nFirst word: ")
    word2 = input("Second word: ")
    check = False
    if len(word1) > 3 : #Checks if user is bad :(
        print("THATS TOO MUCH WORK I hope your pillow is warm on both sides")
        rep = False
        
    if len(word2) > 3:
        print("ur a dum dum")
        rep = False
        
    for i in word1:
        for b in word2:
            if i > b:
                check = True

    if check == True:
        print(word1 + " " + word2)
      
        
    if check == False:
        print(word2 + " " + word1)
       

    end = input("Want to repeat?(y/n): ")
    if end == "n":
        print("bye :(")
        rep = False
            
