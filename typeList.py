L = { "L1": ['magical unicorns',19,'hello',98.98,'world'], "L2": [2,3,1,7,4,12], "L3": ['magical','unicorns']}
temp1 = 0
temp2 = 0
strings=[]
numbers=[]
for i in L: 
    for x in L[i]:
        if type(x) ==  int:
            temp1 += 1
        elif type(x) == str:
            temp2 += 1
    for x in L[i]:
        if temp1 > 0 and temp2 > 0:
            if type(x) == int:
                numbers.append(x)
            if type(x) == str:
                strings.append(x)
        for z in numbers:
            temp3 = 0
            temp3 += z
print numbers
print strings