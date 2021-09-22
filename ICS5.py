#Dum dum data set challenge
#Arya Vishnu
#Evil user doesnt want me to use lists. this makes me very sad 


repeat = True
counter = 0

maxi = 0
mini = 0

while repeat == True:
    data = float(input("-------------\nwhaddya want: "))

    if counter == 0:
        temp1 = data
        
    if counter == 1:
        temp2 = data
        if temp1 >= temp2:
            maxi = temp1
            mini = temp2
        else:
            maxi = temp2
            mini = temp1 
        
    else:
        if data > maxi:
            maxi = data
        if data < mini:
            mini = data
            
    bye = input("Do you want to leave(y/n): ")
   
    if bye == "y":
        if counter == 0:
            print("you didnt put the other number in dum dum")
            repeat = False
        else:
            conclu = (maxi - mini)
            print(str(maxi) + "-" + str(mini))
            print(str(conclu))
            repeat = False
            
    counter += 1
        
    
