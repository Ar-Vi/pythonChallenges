#Bracket Logic
#Arya Vishnu
#Checks if brackets are legal


while True: 
    brackets = input("-----------\nGive me your brackets mortal: ")

    closeB = 0
    openB = 0
    bole = True

    for i in brackets:
        if i == ")":
            closeB += 1
            bole = True
        if i == "(":
            openB += 1
            bole = False
  

    if openB == closeB and bole == True:
        print("that makes me happy")
    if openB != closeB or openB == closeB and bole == False:
        print("ILLEGAL u dum dum")
    if closeB == 0 and openB == 0:
        print("..but you didnt give me any :(")
