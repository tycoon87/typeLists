L = ['magical unicorns',19,'hello',98.98,'world']
x = []
y = []
for i in range(len(L)):
        if type(L[i]) == str:
            x = L[i]
        elif type(L[i]) == int:
            y = L[i]
print(x)
print(y)