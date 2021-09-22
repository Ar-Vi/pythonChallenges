#FIND and REPLACE
#Arya Vishnu
#finding and replacing idk

def find_replace(lst, item1, item2):
    temp_list = []
    for i in lst:
        if i == item1:
            a = item2
        else:
            a = i
        temp_list.append(a)
    
    print(temp_list)

find_replace([1,1,2,2,1], 1, 4)
