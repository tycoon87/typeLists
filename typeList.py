#L = { "L1": ['magical unicorns',19,'hello',98.98,'world'], "L2": [2,3,1,7,4,12], "L3": ['magical','unicorns']}
#temp1 = 0
#temp2 = 0
#strings=[]
#numbers=[]
#for i in L: 
#    for x in L[i]:
#        if type(x) ==  int:
#            temp1 += 1
#        elif type(x) == str:
#            temp2 += 1
#    for x in L[i]:
#        if temp1 > 0 and temp2 > 0:
#            if type(x) == int:
#                numbers.append(x)
#            if type(x) == str:
#                strings.append(x)
#        for z in numbers:
#            temp3 = 0
#            temp3 += z
#print numbers
#print strings

#******************************************************
#set variables
mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]
#define andset a function
def identify_list_type(lst):
#    sex variable new  string to blank
    new_string = ''
#    ste temp nymber to be 0
    total = 0
#    start a for loop
    for value in lst:
#        if the corrent instance's valuse is an intager 
#        or if the instance value is a floating number
        if isinstance(value, int) or isinstance(value, float):
#            set the temparary numver to be the valuse of the               of that instance
            total += value
#        outherwise if the instance is a string 
        elif isinstance(value, str):
#            set the new string value to the instance value
            new_string += value
#    once the variables are set if the array has string             values and intager values
    if new_string and total:
#        print the corrasponding conditions
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total
#        if the vause only have string values
    elif new_string:
#        print the corrasponding conditions
        print "The array you entered is of string type"
        print "String:",new_string
#        outherwise if the value is  only intagers than print           the corrasponding conditions
    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)