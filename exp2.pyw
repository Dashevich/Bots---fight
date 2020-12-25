from tkinter import *
import os
import time
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import subprocess
import socket

times = 500
game = 0
w_w = 1500
w_h = 800
n = 10
count = 0
mas = []
name1 = ""
name2 = ""
host = "localhost"
port = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
conn, addr = server.accept()
# ------------------------------------------------------------------------------
def inp():
    global n

    file = open('input.txt', 'r')
    n = int(file.readline())
    player = file.readline().split('\n')[0]
    for line in file:
        #print(line)
        a = []
        for i in line:
            if i != ' ' and i != '\n':
                a.append(i)
        mas.append(a)
    #print(mas)
    file.close()

    inp_str = ""
    inp_str += (str(n) + '\n')
    inp_str += (str(player))
    for i in range(n):
        inp_str += ('\n')
        for j in range(n):
            inp_str += (str(mas[i][j]) + ' ')
    print(inp_str)

    server.settimeout(1.0)
    conn.send(inp_str.encode("utf-8"))
    print("get")

def outp(player):
    print('o')
    server.settimeout(1.0)
    print('a')
    while True:
        data = conn.recv(1024*10).decode()
        #print('b')
        if data:
            break

    print("put")
    x = int(data.split(' ')[0])
    y = int(data.split(' ')[1])
    mas[x][y] = player
    file = open('output.txt', 'w')
    file.write(str(x) + ' ' + str(y))
    file.close()
    print(mas)


inp()
outp(1)

conn.close()