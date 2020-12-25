from tkinter import *
import os
import time
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import subprocess

times = 500
game = 0
w_w = 1500
w_h = 800
n = 10
mas = [[0] * n for i in range(n)]
count = 0
name1 = ""
name2 = ""
host = "localhost"
port = 1234

def inp(player):
    global n
    file = open('input.txt', 'w')
    file.write(str(n) + '\n')
    file.write(str(player))
    for i in range(n):
        file.write('\n')
        for j in range(n):
            file.write(str(mas[i][j]) + ' ')
    file.close()

def outp(player):
    file = open('output.txt', 'r')
    xy = file.readline()
    file.close()
    x = int(xy.split(' ')[0])
    y = int(xy.split(' ')[1])
    file.close()
    mas[x][y] = player
    print(x, y)
    print(mas)
    file = open('output.txt', 'w')
    file.close()

def draw():
    global n
    for i in range(n):
        for j in range(n):
            if mas[j][i] == 1:
                c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * i + 2, w_h / 4 + w_h / 2 / n * j + 2,
                              (w_w - w_h / 2) / 2 + w_h / 2 / n * (i+1) - 2, w_h / 4 + w_h / 2 / n * (j+1) - 2, fill="red", width=2)
                c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * (i+1) - 2, w_h / 4 + w_h / 2 / n * j + 2,
                              (w_w - w_h / 2) / 2 + w_h / 2 / n * i + 2, w_h / 4 + w_h / 2 / n * (j + 1) - 2, fill="red", width=2)
            if mas[j][i] == 2:
                #c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * i, w_h / 4 + w_h / 2 / n * i, 50, 50)
                c.create_oval((w_w - w_h / 2) / 2 + w_h / 2 / n * i + 2, w_h / 4 + w_h / 2 / n * j + 2,
                              (w_w - w_h / 2) / 2 + w_h / 2 / n * (i+1) - 2, w_h / 4 + w_h / 2 / n * (j+1) - 2, outline="green", width=2)

def check():
    global n
    ind = 3
    for i in range(n):
        for j in range(n):
            if mas[i][j] == 0:
                ind = 0
    for i in range(n):
        for j in range(n):
            if i < n - 4:
                if mas[i][j] == mas[i+1][j] == mas[i+2][j] == mas[i+3][j] == mas[i+4][j] != 0:
                    c.create_line((w_w - w_h / 2) / 2 + w_h / 4 / n * (2*j+1) , w_h / 4 + w_h / 2 / n * i + 2,
                                  (w_w - w_h / 2) / 2 + w_h / 4 / n * (2*j+1) , w_h / 4 + w_h / 2 / n * (i+5) - 2 , fill="black", width=3)
                    if mas[i][j] == 1:
                        ind = 1
                    else:
                        ind = 2
                    return ind
            if j < n - 4:
                if mas[i][j] == mas[i][j+1] == mas[i][j+2] == mas[i][j+3] == mas[i][j+4] != 0:
                    c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * j + 2, w_h / 4 + w_h / 4 / n * (2*i+1) ,
                                  (w_w - w_h / 2) / 2 + w_h / 2 / n * (j+5) - 2, w_h / 4 + w_h / 4 / n * (2*i+1),fill="black", width=3)
                    if mas[i][j] == 1:
                        ind = 1
                    else:
                        ind = 2
                    return ind
            if i < n - 4 and j < n - 4:
                if mas[i][j] == mas[i+1][j+1] == mas[i+2][j+2] == mas[i+3][j+3] == mas[i+4][j+4] != 0:
                    c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * j + 2, w_h / 4 + w_h / 2 / n * i + 2,
                                  (w_w - w_h / 2) / 2 + w_h / 2 / n * (j + 5) - 2, w_h / 4 + w_h / 2 / n * (i+5) - 2, fill="black", width=3)
                    if mas[i][j] == 1:
                        ind = 1
                    else:
                        ind = 2
                    return ind
            if i >= 4 and j < n - 4:
                if mas[i][j] == mas[i-1][j+1] == mas[i-2][j+2] == mas[i-3][j+3] == mas[i-4][j+4] != 0:
                    c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * (j) + 2, w_h / 4 + w_h / 2 / n * (i+1) - 2,
                                  (w_w - w_h / 2) / 2 + w_h / 2 / n * (j + 5) - 2, w_h / 4 + w_h / 2 / n * (i-4) + 2, fill="black", width=3)
                    if mas[i][j] == 1:
                        ind = 1
                    else:
                        ind = 2
                    return ind
    return ind

def game(count):
    global ans, name1, name2
    xy = ''
    if count % 2 == 0:
        player = 1
        inp(player)
        os.startfile("exp2.pyw")
        os.startfile(name1)
    else:
        player = 2
        inp(player)
        os.startfile("exp2.pyw")
        os.startfile(name2)

    time.sleep(1)
    outp(player)
    draw()
    ans = check()

  #  check()
def play():
    global ans
    combo.configure(state=DISABLED)
    ans = 1
    count = 0
    while True:
        window.update()
        window.after(times, game(count))
        print(ans)
        if ans != 0:
            if ans == 1:
                lb = Label(text=name1.rsplit('/', 1)[1].split('.')[0] + " win", bg="white")
            if ans == 2:
                lb = Label(text=name2.rsplit('/', 1)[1].split('.')[0] + " win", bg="white")
            if ans == 3:
                lb = Label(text="draw", bg="white")
            lb.config(font=("Courier", 44))
            lb.place(x=w_w/2 - 250, y=100, width=600, height=45)

            break
        count += 1

def open_file():
    global name1, name2
    filepath = askopenfilename(
        filetypes=[("Py Files", "*.py*"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    #txt_edit.delete("1.0", END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        #txt_edit.insert(END, text)
    window.title(f"Simple Text Editor - {filepath}")
    if name1 == "":
        name1 = filepath
        lb1 = Label(text=name1.rsplit('/', 1)[1], bg="white")
        lb1.config(font=("Courier", 20))
        lb1.place(x=w_w/8-20, y=300, width=300, height=50)
        #name1 = str(host) + '/' + name1
    else:
        name2 = filepath
        lb2 = Label(text=name2.rsplit('/', 1)[1], bg="white")
        lb2.config(font=("Courier", 20))
        lb2.place(x=w_w/8*6-20, y=300,  width=300, height=50)
        #name2 = str(host) + '/' + name2

def on_select(event=None):
    global n, mas
    if event:
        for i in range(n + 1):
            c.create_line((w_w - w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i, (w_w + w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i, fill ="white")
            c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * i, w_h / 4, (w_w - w_h / 2) / 2 + w_h / 2 / n * i,3 * w_h / 4, fill="white")

        n = int(combo.get())
        for i in range(n + 1):
            c.create_line((w_w - w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i, (w_w + w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i)
            c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * i, w_h / 4, (w_w - w_h / 2) / 2 + w_h / 2 / n * i,3 * w_h / 4)
        mas = [[0] * n for i in range(n)]

window = Tk()
window.geometry('{}x{}'.format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.title("Cross and Zeros")
c = Canvas(window, width=w_w, height=w_h, bg='white')
c.pack()

for i in range(n + 1):
    c.create_line((w_w - w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i, (w_w + w_h / 2) / 2, w_h / 4 + w_h / 2 / n * i)
    c.create_line((w_w - w_h / 2) / 2 + w_h / 2 / n * i, w_h / 4, (w_w - w_h / 2) / 2 + w_h / 2 / n * i, 3 * w_h / 4)

start = time.time()
c.create_line(w_w/8+10, 100-20, w_w/8+110, 200-20, fill="red", width=4)
c.create_line(w_w/8+10, 200-20, w_w/8+110, 100-20, fill="red", width=4)
c.create_oval(w_w/8*6+10, 100-20, w_w/8*6+110, 200-20, outline="green", width=4)
btn_start = Button(window, text="Начать", command=play, width=20, height=3)
btn_open1 = Button(window, text="Открыть", command=open_file, width=20, height=3)
btn_open2 = Button(window, text="Открыть", command=open_file, width=20, height=3)
btn_open1.place(x=w_w/8, y=200)
btn_open2.place(x=w_w/8*6, y=200)
btn_start.place(x=700, y=700)

combo = Combobox(window)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
combo.current(2)
combo.place(x=700, y=650)
combo.bind('<<ComboboxSelected>>', on_select)

window.mainloop()
