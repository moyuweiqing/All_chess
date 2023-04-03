from tkinter import *
import tkinter.messagebox  # 弹窗库
import numpy as np
from tkinter.messagebox import showinfo

root = Tk()
root.title("中国象棋")

chessdic = {
    1 : '兵'
    ,2 : '炮'
    ,3 : '馬'
    ,4 : '車'
    ,5 : '相'
    ,6 : '仕'
    ,7 : '帅'
    ,11 : '卒'
    ,12 : '砲'
    ,13 : '馬'
    ,14 : '車'
    ,15 : '象'
    ,16 : '士'
    ,17 : '将'
}

A=np.full((10,9),0)
B=np.full((10,9),0)

cnt = 0
last_i = 0
last_j = 0

w1 = Canvas(root, width=630,height=700,background='lightcyan')
w1.pack()

def draw_chessboard():
    for i in range(0, 9):
        if i == 0 or i == 8:
            w1.create_line(i * 70 + 35, 35, i * 70 + 35, 665)
        else:
            w1.create_line(i * 70 + 35, 35, i * 70 + 35, 315)
            w1.create_line(i * 70 + 35, 385, i * 70 + 35, 665)
    for i in range(0, 10):
        w1.create_line(35, i * 70 + 35, 595, i * 70 + 35)

    w1.create_line(245, 35, 385, 175)
    w1.create_line(385, 35, 245, 175)
    w1.create_line(245, 525, 385, 665)
    w1.create_line(385, 525, 245, 665)
    w1.create_text(175, 350, text='楚   河', font=('华文隶书', 50))
    w1.create_text(455, 350, text='汉   界', font=('华文隶书', 50))

def draw_chesses():
    global A, B
    A[6][0] = 1
    A[6][2] = 1
    A[6][4] = 1
    A[6][6] = 1
    A[6][8] = 1

    A[7][1] = 2
    A[7][7] = 2

    A[9][0] = 4
    A[9][1] = 3
    A[9][2] = 5
    A[9][3] = 6
    A[9][4] = 7
    A[9][5] = 6
    A[9][6] = 5
    A[9][7] = 3
    A[9][8] = 4

    A[3][0] = 11
    A[3][2] = 11
    A[3][4] = 11
    A[3][6] = 11
    A[3][8] = 11

    A[2][1] = 12
    A[2][7] = 12

    A[0][0] = 14
    A[0][1] = 13
    A[0][2] = 15
    A[0][3] = 16
    A[0][4] = 17
    A[0][5] = 16
    A[0][6] = 15
    A[0][7] = 13
    A[0][8] = 14

    B[6][0] = 1
    B[6][2] = 1
    B[6][4] = 1
    B[6][6] = 1
    B[6][8] = 1

    B[7][1] = 1
    B[7][7] = 1

    B[9][0] = 1
    B[9][1] = 1
    B[9][2] = 1
    B[9][3] = 1
    B[9][4] = 1
    B[9][5] = 1
    B[9][6] = 1
    B[9][7] = 1
    B[9][8] = 1

    B[3][0] = 2
    B[3][2] = 2
    B[3][4] = 2
    B[3][6] = 2
    B[3][8] = 2

    B[2][1] = 2
    B[2][7] = 2

    B[0][0] = 2
    B[0][1] = 2
    B[0][2] = 2
    B[0][3] = 2
    B[0][4] = 2
    B[0][5] = 2
    B[0][6] = 2
    B[0][7] = 2
    B[0][8] = 2

def draw_chesses2(A, B):
    global w1
    for i in range(0, len(A[0])):
        for j in range(0, len(A)):
            if A[j][i] > 0:
                if j == last_j and i == last_i:
                    w1.create_oval(70 * i + 5, 70 * j + 5, 70 * i + 65, 70 * j + 65, fill='green')
                    w1.create_oval(70 * i + 9, 70 * j + 9, 70 * i + 61, 70 * j + 61, fill='green')
                else:
                    w1.create_oval(70 * i + 5, 70 * j + 5, 70 * i + 65, 70 * j + 65, fill='white')
                    w1.create_oval(70 * i + 9, 70 * j + 9, 70 * i + 61, 70 * j + 61, fill='white')
                if B[j][i] == 2:
                    w1.create_text(70*i+35, 70*j+35, text=chessdic[A[j][i]], fill='black', font=('华文中宋', 25))
                if B[j][i] == 1:
                    w1.create_text(70*i+35, 70*j+35, text=chessdic[A[j][i]], fill='red', font=('华文中宋', 25))

def chess_if_success(j0, i0, j1, i1):
    global A, B

    # 4 14
    if A[j0][i0] == 4 or A[j0][i0] == 14:
        if j0 != j1 and i0 != i1:
            return 0
        else:
            if j0 == j1 and i0 != i1:
                if i0 > i1:
                    for i in range(i1 + 1, i0):
                        if A[j0][i] > 0:
                            return 0
                else:
                    for i in range(i0 + 1, i1):
                        if A[j0][i] > 0:
                            return 0

            if j0 != j1 and i0 == i1:
                if j0 > j1:
                    for i in range(j1 + 1, j0):
                        if A[i][i0] > 0:
                            return 0
                else:
                    for i in range(j0 + 1, j1):
                        if A[i][i0] > 0:
                            return 0
            return 1

    # 2 12
    elif A[j0][i0] == 2 or A[j0][i0] == 12:
        if j0 != j1 and i0 != i1:
            return 0
        else:
            tmpn = 0
            if j0 == j1 and i0 != i1:
                if i0 > i1:
                    for i in range(i1 + 1, i0):
                        if A[j0][i] > 0:
                            tmpn += 1
                else:
                    for i in range(i0 + 1, i1):
                        if A[j0][i] > 0:
                            tmpn += 1
                if tmpn > 1:
                    return 0
                elif tmpn == 1:
                    if B[j1][i1] != B[j0][i0]:
                        return 1
                    else:
                        return 0
                else:
                    if A[j1][i1] == 0:
                        return 1
                    else:
                        return 0

        if j0 != j1 and i0 == i1:
            if j0 > j1:
                for j in range(j1 + 1, j0):
                    if A[j][i0] > 0:
                        tmpn += 1
            else:
                for j in range(j0 + 1, j1):
                    if A[j][i0] > 0:
                        tmpn += 1
            if tmpn > 1:
                return 0
            elif tmpn == 1:
                if B[j1][i1] != B[j0][i0]:
                    return 1
                else:
                    return 0
            else:
                if A[j1][i1] == 0:
                    return 1
                else:
                    return 0

    # 1 11
    elif A[j0][i0] == 1 or A[j0][i0] == 11:
        tmpn = 0
        if B[j0][i0] == 1:
            if j0 <= 4:
                tmpn = 1
        else:
            if j0 >= 5:
                tmpn = 1

        if B[j0][i0] == 1:
            if tmpn == 0:
                if j0 - j1 == 1 and i0 == i1:
                    if B[j1][i1] != B[j0][i0]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                if i0 == i1:
                    if j0 - j1 == 1:
                        if B[j1][i1] != B[j0][i0]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
                else:
                    if abs(i0 - i1) == 1:
                        if B[j1][i1] != B[j0][i0]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
        elif B[j0][i0] == 2:
            if tmpn == 0:
                if j1 - j0 == 1 and i0 == i1:
                    if B[j1][i1] != B[j0][i0]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                if i0 == i1:
                    if j1 - j0 == 1:
                        if B[j1][i1] != B[j0][i0]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
                else:
                    if abs(i1 - i0) == 1:
                        if B[j1][i1] != B[j0][i0]:
                            return 1
                        else:
                            return 0
                    else:
                        return 0

    # 5 15
    elif A[j0][i0] == 5 or A[j0][i0] == 15:
        if B[j0][i0] == 1:
            if j1 <= 4:
                return 0
        else:
            if j1 >= 5:
                return 0
        if abs(j0 - j1) == 2 and abs(i0 - i1) == 2:
            if B[j0][i0] != B[j1][i1]:
                if A[int((j0+j1)/2)][int((i0+i1)/2)] == 0:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0

    # 7 17
    elif A[j0][i0] == 7 or A[j0][i0] == 17:
        if B[j0][i0] == 1:
            if j1 >= 7 and j1 <= 9 and 3 <= i1 and i1 <= 5:
                if j0 == j1 and abs(i0 - i1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                elif i0 == i1 and abs(j0 - j1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0

        if B[j0][i0] == 2:
            if j1 >= 0 and j1 <= 2 and 3 <= i1 and i1 <= 5:
                if j0 == j1 and abs(i0 - i1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                elif i0 == i1 and abs(j0 - j1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0

    # 6 16
    elif A[j0][i0] == 6 or A[j0][i0] == 16:
        if B[j0][i0] == 1:
            if j1 >= 7 and j1 <= 9 and 3 <= i1 and i1 <= 5:
                if abs(j0 - j1) == 1 and abs(i0 -i1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0

        if B[j0][i0] == 2:
            if j1 >= 0 and j1 <= 2 and 3 <= i1 and i1 <= 5:
                if abs(j0 - j1) == 1 and abs(i0 -i1) == 1:
                    if B[j0][i0] != B[j1][i1]:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0

    # 3 13
    elif A[j0][i0] == 3 or A[j0][i0] == 13:
        tmp1 = abs(j0-j1)
        tmp2 = abs(i0-i1)
        if tmp1 == 2 and tmp2 == 1:
            if A[int((j0 + j1) / 2)][i0] == 0:
                if B[j0][i1] != B[j1][i0]:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif tmp1 == 1 and tmp2 == 2:
            if A[i0][int(j0 + j1) / 2] == 0:
                if B[j0][i1] != B[j1][i0]:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0

def if_win():
    global w1, A
    shuai = 0
    jiang = 0
    for j in range(0, len(A)):
        for i in range(0, len(A[0])):
            if A[j][i] == 7:
                shuai += 1
            elif A[j][i] == 17:
                jiang += 1
    if shuai == 0:
        return 1
    elif jiang == 0:
        return 2
    else:
        return 0

def step1(j, i):
    global A, B
    if B[j][i] == 1:
        return 1
    else:
        return 0

def step2(j, i):
    global A, B, last_i, last_j
    if B[j][i] == 1:
        last_i = i
        last_j = j
        w1.delete("all")
        draw_chessboard()
        draw_chesses2(A, B)
        return 0
    else:
        r = chess_if_success(last_j, last_i, j, i)
        if r == 1:
            t = A[last_j][last_i]
            A[last_j][last_i] = 0
            B[last_j][last_i] = 0
            A[j][i] = t
            B[j][i] = 1
    
            w1.delete("all")
            draw_chessboard()
            draw_chesses2(A, B)
            return 1
        else:
            return 0

def step3(j, i):
    global A, B
    if B[j][i] == 2:
        return 1
    else:
        return 0

def step4(j, i):
    global A, B, last_i, last_j
    if B[j][i] == 2:
        return 0
    else:
        r = chess_if_success(last_j, last_i, j, i)
        if r == 1:
            t = A[last_j][last_i]
            A[last_j][last_i] = 0
            B[last_j][last_i] = 0
            A[j][i] = t
            B[j][i] = 2

            w1.delete("all")
            draw_chessboard()
            draw_chesses2(A, B)
            return 1
        else:
            return 0


def callback(event):
    global cnt, last_i, last_j

    for j in range (0,len(A)): #双重循环定位点击位置最近的网格线交点（i，j），保证棋子落在线的交点处。
        for i in range (0,len(A[0])):
            if (event.x - 35 - 70 * i) ** 2 + (event.y - 35 - 70 * j) ** 2 <= 2 * 35 ** 2:
                break
        if (event.x - 35 - 70 * i) ** 2 + (event.y - 35 - 70 * j) ** 2 <= 2* 35 ** 2:
            break

    if cnt % 4 == 0:
        r = step1(j, i)
        if r == 1:
            last_i = i
            last_j = j
            w1.delete('all')
            draw_chessboard()
            draw_chesses2(A, B)
            tmp_cnt = 1
        else:
            tmp_cnt = 0
    if cnt % 4 == 1:
        r = step2(j, i)
        if r == 1:
            tmp_cnt = 1
        else:
            tmp_cnt = 0
        pass
    if cnt % 4 == 2:
        r = step3(j, i)
        if r == 1:
            last_i = i
            last_j = j
            w1.delete('all')
            draw_chessboard()
            draw_chesses2(A, B)
            tmp_cnt = 1
        else:
            tmp_cnt = 0
    if cnt % 4 == 3:
        r = step4(j, i)
        if r == 1:
            tmp_cnt = 1
        else:
            tmp_cnt = 0
        pass
    cnt += tmp_cnt

    win = if_win()
    if win == 1:
        showinfo('提示', '黑方获胜')
    elif win == 2:
        showinfo('提示', '红方获胜')

# draw
draw_chessboard()
draw_chesses()
draw_chesses2(A, B)

#
w1.bind("<Button -1>", callback)
mainloop()