import random
x = -1
y = -1
mas = []

file = open('input.txt', 'r')
n = int(file.readline())
your = file.readline()
for line in file:
    #print(line)
    a = []
    for i in line:
        if i != ' ' and i != '\n':
            a.append(i)
    mas.append(a)
#print(mas)

for i in range(n):
    for j in range(n):
        if mas[i][j] == '0':
            x = i
            y = j
            break
        #print(i, j, mas[i][j])
    if x != -1:
        break
file.close

x1 = random.randint(0,n-1)
y1 = random.randint(0,n-1)
if mas[x1][y1] == '0':
    x = x1
    y = y1
file = open('output.txt', 'w')
file.write(str(x) + ' ' + str(y))
file.close()