from tkinter import *
import tkinter.messagebox  # 弹窗库
import numpy as np
import random

root = Tk()                 # 创建窗口
root.geometry('280x280')
root.title("2048")          # 窗口名字
w1 = Canvas(root, width=280,height=280,background='lightcyan')
w1.pack()

A=np.full((4,4),0)          # 储存数字
B=np.full((4,4),0)          # 记录状态

score = 0                   # 记录总分

# 色块映射情况
num_color_dic = {
    '2': '#FFFF00',
    '4': '#FFCC33',
    '8': '#FF9900',
    '16': '#FF33FF',
    '32': '#66CCFF',
    '64': '#66CC00',
    '128': '#33CC33',
    '256': '#009999',
    '512': '#666699',
    '1024': '#6633FF',
    '2048': '#6600FF',
    '4096': '#660066',
    '8192': '#006644',
    '16384': '#669999',
    '32768': '#336633',
    '65536': '#0033FF'
}

# 画线和画格子
for i in range(0, 5):
    w1.create_line(i * 60 + 20, 20, i * 60 + 20, 260)
    w1.create_line(20, i * 60 + 20, 260, i * 60 + 20)
for j in range(0, 4):
    for i in range(0, 4):
        w1.create_rectangle(i * 60 + 22, j * 60 + 22, i * 60 + 78, j * 60 + 78, fill='#FFFFCC')

# 计算分数
def cal_score():
    global A, score
    score = np.sum(A)

# 重新画线
def re_draw():
    global A, B, w1

    for i in range(0, 5):
        w1.create_line(i * 60 + 20, 20, i * 60 + 20, 260)
        w1.create_line(20, i * 60 + 20, 260, i * 60 + 20)
    for i in range(0, 4):
        for j in range(0, 4):
            if B[i][j] == 0:
                # 注意画布和矩阵之间的对应关系
                w1.create_rectangle(j * 60 + 22, i * 60 + 22, j * 60 + 78, i * 60 + 78, fill='#ADD8E6')
            else:
                w1.create_rectangle(j * 60 + 22, i * 60 + 22, j * 60 + 78, i * 60 + 78, fill=num_color_dic[str(A[i][j])])
                w1.create_text(j * 60 + 50, i * 60 + 50, text=A[i][j], font=('宋体', 20), fill='#000000')

# 生成随机的数字
def make_random_num():
    global A, B, w1

    # 获取所有的空格
    nullblock_list = []
    nullblocks = np.where(B == 0)
    for i in zip(list(nullblocks[0]), list(nullblocks[1])):
        nullblock_list.append(i)

    # 判断是否没空格
    if len(nullblock_list) == 0:
        tkinter.messagebox.showinfo('提示', '游戏结束，你的分数是：' + str(score))

    # 随机是2或者是4
    randint = random.randint(0, 10)
    num = 2 if randint != 9 else 4
    randint = random.randint(0, len(nullblock_list) - 1)

    # 获取随机的位置x和y
    x = nullblock_list[randint][0]
    y = nullblock_list[randint][1]
    A[x][y] = num
    B[x][y] = 1

    # 重新画图和计算分数
    re_draw()
    cal_score()

# 将列表重新排序，有数据的在前面，没数据的在后面
def list_order(alist):
    blist = list(filter(lambda x: x > 0, alist))
    clist = list(filter(lambda x: x == 0, alist))
    dlist = blist + clist
    return dlist

def list_merge(alist):
    # 排序->相加->再排序
    alist = list_order(alist)
    for i in range(0, len(alist) - 1):
        j = i + 1
        if alist[j] > 0:
            if alist[j] == alist[i]:
                alist[i] += alist[j]
                alist[j] = 0
    alist = list_order(alist)
    return alist



def right_press(event):
    global A, B

    # 先保存原矩阵
    raw_A = A

    raw_list = A.tolist()
    new_list = [list(reversed(list_merge(list(reversed(i))))) for i in raw_list]
    A = np.array(new_list)

    B = np.full((4, 4), 0)
    nullblocks = np.where(A > 0)
    for i in zip(list(nullblocks[0]), list(nullblocks[1])):
        B[i[0]][i[1]] = 1

    if (A == raw_A).all() == False:
        make_random_num()

def left_press(event):
    global A, B

    # 先保存原矩阵
    raw_A = A

    raw_list = A.tolist()
    new_list = [list_merge(i) for i in raw_list]
    A = np.array(new_list)

    B = np.full((4, 4), 0)
    nullblocks = np.where(A > 0)
    for i in zip(list(nullblocks[0]), list(nullblocks[1])):
        B[i[0]][i[1]] = 1

    if (A == raw_A).all() == False:
        make_random_num()

def up_press(event):
    global A, B

    # 先保存原矩阵
    raw_A = A

    A = np.transpose(A)
    raw_list = A.tolist()
    new_list = [list_merge(i) for i in raw_list]
    A = np.array(new_list)
    A = np.transpose(A)

    B = np.full((4, 4), 0)
    nullblocks = np.where(A > 0)
    for i in zip(list(nullblocks[0]), list(nullblocks[1])):
        B[i[0]][i[1]] = 1

    if (A == raw_A).all() == False:
        make_random_num()

def down_press(event):
    global A, B

    # 先保存原矩阵
    raw_A = A

    A = np.transpose(A)
    raw_list = A.tolist()
    new_list = [list(reversed(list_merge(list(reversed(i))))) for i in raw_list]
    A = np.array(new_list)
    A = np.transpose(A)

    B = np.full((4, 4), 0)
    nullblocks = np.where(A > 0)
    for i in zip(list(nullblocks[0]), list(nullblocks[1])):
        B[i[0]][i[1]] = 1

    if (A == raw_A).all() == False:
        make_random_num()

make_random_num()

root.bind("<KeyPress-Right>", right_press)
root.bind("<KeyPress-Up>", up_press)
root.bind("<KeyPress-Left>", left_press)
root.bind("<KeyPress-Down>", down_press)

mainloop()