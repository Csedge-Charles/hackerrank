import sys
 
for line in sys.stdin:
    if 'q' == line.rstrip():
        break

line = list(str(line))

amount_list = []
amount = 1
num_list = []

for i in range(len(line) - 1):
    i += 1
    if line[i - 1] == line[i]: #if repeats
        amount += 1 
    
    else:
        num_list.append(int(line[i - 1])) #number gets added into num_list 
        amount_list.append(int(amount)) #amount gets stored in amount_list
        amount = 1 #amount gets reseted
        
amount_list.append(int(amount)) #left over value in amount gets stored back in amount_list
num_list.append(int(line[i - 1])) #same for num_list


tup_set = '' #Variable where tuples are store in
for i in range(len(amount_list)): #Goes throught amount_list
    tup_set += str((amount_list[i], num_list[i])) #Adds tuple 
    tup_set += ' ' #Adds space between tuples

print(tup_set)

