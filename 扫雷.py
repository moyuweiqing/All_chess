from tkinter import *
import tkinter.messagebox  # 弹窗库
import numpy as np
import random
from tkinter.messagebox import showinfo
import time

root = Tk()     # 创建窗口
root.title("扫雷")        # 窗口名字

lei_num = 10

A=np.full((10,10),0)  # 储存已有雷的矩阵位置
B=np.full((10,10),0)  # 用来记录每个位置棋子的状态

flagnum = 0

w1 = Canvas(root, width=440,height=440,background='lightcyan')
w1.pack()

a = random.sample(range(0, 100), lei_num)
for i in a:
    x = i // 10
    y = i % 10
    A[y][x] = 1

for i in range(0,11):
    w1.create_line(i * 40 + 20, 20, i * 40 + 20, 420)
    w1.create_line(20, i * 40 + 20, 420, i * 40 + 20)
for j in range(0, 10):
    for i in range(0, 10):
        w1.create_rectangle(i * 40 + 22, j * 40 + 22, i * 40 + 58, j * 40 + 58, fill='#ADD8E6')

def getleinum(x, y):
    global A, B
    lei = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if i < 0 or j < 0 or i > 9 or j > 9:
                continue
            else:
                lei += A[i][j]

    B[y][x] = 1
    w1.create_rectangle(x * 40 + 22, y * 40 + 22, x * 40 + 58, y * 40 + 58, fill='lightcyan')
    if lei != 0:
        w1.create_text(x * 40 + 40, y * 40 + 40, text=str(lei), font=('华文隶书', 20))
    else:
        pass

    if lei == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                x0 = x + i
                y0 = y + j
                if x0 < 0 or y0 < 0 or x0 > 9 or y0 > 9:
                    continue
                else:
                    if B[y0][x0] == 0:
                        getleinum(x0, y0)

    return

def callback(event):        #输入的是点击事件，event.x和event.y是鼠标点击事件的位置
    global A, B
    x = (event.x - 20) // 40
    y = (event.y - 20) // 40

    if x < 10 and y < 10:
        if B[y][x] != 2:
            if A[y][x] == 1:
                w1.create_rectangle(x * 40 + 22, y * 40 + 22, x * 40 + 58, y * 40 + 58, fill='lightcyan')
                w1.create_text(x * 40 + 40, y * 40 + 40, text='雷', font=('华文隶书', 20))
                B[y][x] = 1
                tkinter.messagebox.showinfo('提示', '挑战失败')

            if A[y][x] == 0:
                getleinum(x, y)

def callback2(event):
    global A, B, flagnum
    x = (event.x - 20) // 40
    y = (event.y - 20) // 40

    if x < 10 and y < 10:
        if B[y][x] == 2:
            B[y][x] = 0
            w1.create_rectangle(x * 40 + 22, y * 40 + 22, x * 40 + 58, y * 40 + 58, fill='#ADD8E6')
            flagnum -= 1
        elif B[y][x] != 1 and B[y][x] != 2:
            B[y][x] = 2
            w1.create_text(x * 40 + 40, y * 40 + 40, text='旗', font=('华文隶书', 20))
            flagnum += 1
    if flagnum == lei_num:
        for i in a:
            x = i // 10
            y = i % 10
            if B[y][x] != 2:
                return
        tkinter.messagebox.showinfo('提示', '挑战成功')


w1.bind("<Button -1>", callback)
w1.pack()

w1.bind("<Button -3>", callback2)
w1.pack()

mainloop()