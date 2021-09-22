#LETTER COUNTER
#Arya Vishnu
#Counts the letters that occur the most

let = {}

sent = input("GIVE: ")


for i in sent:
    if i in let:
        temp = let[i]
        temp += 1
        let[i] = temp
    else:
        if i != " " and i != "." and i != "?" and i != "!" and i != "," and i != "/":
            let[i] = 1
        
mostLet = max(let, key = let.get)
letNum = let[mostLet]

#handle ties with an for i, that goes thru the list?

for i in let:
    if letNum == let[i]:
        print(i + " occured " + str(letNum) + " time(s)")
        
