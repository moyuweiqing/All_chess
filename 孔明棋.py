from tkinter import *
import tkinter.messagebox  # 弹窗库
import numpy as np

root = Tk()                                     # 创建窗口
root.title("孔明棋")                            # 窗口名字
w1 = Canvas(root, width=320, height=320, background='lightcyan')
w1.pack()

judge = True
chosen_x = 0
chosen_y = 0

# 储存棋子的矩阵，默认为-1
A=np.full((7,7),-1)

# 棋盘初始化
def chess_ini():
    # 有棋子的部分 1
    # 无棋子的部分 0
    # 不可下的部分 -1
    global A
    for i in range(0, 7):
        for j in range(2, 5):
            A[i][j] = 1
            A[j][i] = 1
    A[3][3] = 0
    # print(A)

# 画棋盘
def draw_chessboard():
    global A, w1
    w1.delete('all')
    # for i in range(2, 6):
    #     w1.create_line(i * 40 + 20, 20, i * 40 + 20, 300)
    #     w1.create_line(20, i * 40 + 20, 300, i * 40 + 20)
    for j in range(0, 7):
        for i in range(2, 5):
            w1.create_rectangle(i * 40 + 22, j * 40 + 22, i * 40 + 58, j * 40 + 58, fill='#ADD8E6')
            w1.create_rectangle(j * 40 + 22, i * 40 + 22, j * 40 + 58, i * 40 + 58, fill='#ADD8E6')
    for i in range(0, 7):
        for j in range(0, 7):
            if A[j][i] == 1:
                if i == chosen_x and j == chosen_y:
                    w1.create_oval(i * 40 + 25, j * 40 + 25, i * 40 + 55, j * 40 + 55, fill='yellow')
                else:
                    w1.create_oval(i * 40 + 27, j * 40 + 27, i * 40 + 53, j * 40 + 53, fill='yellow')
            elif A[j][i] == 0:
                w1.create_oval(i * 40 + 25, j * 40 + 25, i * 40 + 55, j * 40 + 55, fill='brown')

# 判断是否能走
def check(new_x, new_y):
    if (abs(new_x - chosen_x) == 2 and new_y == chosen_y) or (abs(new_y - chosen_y) == 2 and new_x == chosen_x):
        return True
    else:
        return False

# 选择棋子走动
def callback(event):
    global A, judge, chosen_x, chosen_y
    x = (event.x - 20) // 40
    y = (event.y - 20) // 40

    if A[y][x] == 1:
        chosen_x = x
        chosen_y = y
        judge = False
    if A[y][x] == 0:
        if check(x, y):
            if A[int((y + chosen_y) / 2)][int((x + chosen_x) / 2)] == 1:
                A[y][x] = 1
                A[int((y + chosen_y) / 2)][int((x + chosen_x) / 2)] = 0
                A[chosen_y][chosen_x] = 0
    draw_chessboard()

chess_ini()
draw_chessboard()
w1.bind("<Button -1>", callback)
w1.pack()
mainloop()