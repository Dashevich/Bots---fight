import random
import socket

message = "hello world"
sock = socket.socket()
sock.connect(('localhost', 1234))

x = -1
y = -1
mas = []

data = sock.recv(1024*10).decode()
#data = "10\n1\n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0"
n = int(data.split('\n')[0])
list = data.split('\n')
#print(list)
your = data.split('\n')[1]
data = data.split('\n')[2:]
#print(data)
for line in data:
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

x1 = random.randint(0,n-1)
y1 = random.randint(0,n-1)
if mas[x1][y1] == '0':
    x = x1
    y = y1
#print(x, y, n)

message = str(x) + ' ' + str(y)
sock.send(message.encode("utf-8"))
sock.close()
print('1')