#LUCKY 7s
#Arya Vishnu
#Virtual Dice I guess

import random

while True:
    count7 = 0
    rolls = int(input("---------------\nHow many rolls: "))

    for i in range(0, rolls):
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        add = r1 + r2
        print("(" + str(r1) + ", " + str(r2)+ ")" + ";" + "sum " + str(add))
        if add == 7:
            count7 += 1

    print(str(count7) + " seven(s) were rolled")
