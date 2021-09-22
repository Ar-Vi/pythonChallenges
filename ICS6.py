#baby 
#Arya Vishnu
#Stimulates the worst type of baby, a math baby
import random

repeat = True
f = 5
m = -1

while repeat == True:

    chance = random.randint(0,10)
    

    if chance >= 1 and chance <= 7:
        f -= 1
        m -= 1
        print("steps towards pa")     
    if chance > 7 and chance <= 10:
        m += 1
        f += 1
        print("steps towards mum")
        
    if m >= 0:
        print("Infant went to mumther!")
        repeat = False
    if f <= 0:
        print("Infant went to Pa!")
        repeat = False
        
