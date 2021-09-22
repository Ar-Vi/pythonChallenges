#SALES COMMISSION
#Arya V
#Calculates Sales rep ann earnings
repeat = True

while repeat == True:
    
    sal = float(input("What was your total amount of sales: "))
    earn = 35000

    if sal < 0:
        print("sales isnt for you")

    if sal >= 200000:
        earn += 20000

    if sal >= 400000:
        earn += 40000

    if sal > 400000:
        calc = sal - 400000
        print(calc)
        calc *= 0.25
        earn += calc

    if sal > 1000000:
        earn += 50000

    print("Here is your commission: " + str(earn))

    loop = input("Do you want to do it again?(t = again, f = bye)")

    if loop == "f":
        print("bye >:(")
        repeat = False

