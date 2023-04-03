from tkinter import *
import tkinter.messagebox  # 弹窗库
import numpy as np
import random

root = Tk()                                     # 创建窗口
root.title("黑白棋")                            # 窗口名字
w1 = Canvas(root, width=500, height=360, background='lightcyan')
w1.pack()

# 储存棋子的矩阵，空位为0
A=np.full((8,8),0)

# 初始化白色的棋子，白色为1
A[3][3] = 1
A[4][4] = 1
# 初始化黑色的棋子，黑色为2
A[3][4] = 2
A[4][3] = 2

# 游戏结束和顺序
if_over = False
if_black = True

# 当前可能下的位置
now_location_dic = {}

# 初始化画图
for i in range(0,9):
    w1.create_line(i * 40 + 20, 20, i * 40 + 20, 340)
    w1.create_line(20, i * 40 + 20, 340, i * 40 + 20)
for j in range(0,8):
    for i in range(0,8):
        w1.create_rectangle(i * 40 + 22, j * 40 + 22, i * 40 + 58, j * 40 + 58, fill='#ADD8E6')

# label分布
turntext = StringVar()
label1text = StringVar()
label2text = StringVar()
turntext.set('现在轮到：黑方')
label1text.set('白棋个数：2')
label2text.set('黑棋个数：2')
turn = Label(w1, textvariable=turntext, font=('黑体', 12)).place_configure(x=350, y=60)
label1 = Label(w1, textvariable=label1text, font=('黑体', 12)).place_configure(x=350, y=150)
label2 = Label(w1, textvariable=label2text, font=('黑体', 12)).place_configure(x=350, y=200)
button = Button(w1, command=lambda :cancel(), text='撤销').place_configure(x=350, y=250)
last_A = A

# 撤销，上一步
def cancel():
    global A, if_black, last_A, now_location_dic
    A = last_A
    if_black = not if_black
    possible_location_dic = get_possible_location(if_black)
    now_location_dic = possible_location_dic
    draw_chess(possible_location_dic)
    cal()
    print(if_black, now_location_dic)

# 统计次数
def cal():
    global turntext, label1text, label2text
    w_cnt = A[A==1].sum()
    b_cnt = int(A[A==2].sum()/2)
    if if_black:
        turntext.set('现在轮到：黑方')
    else:
        turntext.set('现在轮到：白方')
    label1text.set('白棋个数：' + str(w_cnt))
    label2text.set('黑棋个数：' + str(b_cnt))

# 画棋子
def draw_chess(possible_location_dic):
    global w1
    w1.delete('all')
    for i in range(0, 9):
        w1.create_line(i * 40 + 20, 20, i * 40 + 20, 340)
        w1.create_line(20, i * 40 + 20, 340, i * 40 + 20)
    for j in range(0, 8):
        for i in range(0, 8):
            w1.create_rectangle(i * 40 + 22, j * 40 + 22, i * 40 + 58, j * 40 + 58, fill='#ADD8E6')

    xylist = [(i, j) for j in range(0, 8) for i in range(0, 8)]
    for x, y in xylist:
        if A[y][x] == 1:
            w1.create_oval(x * 40 + 25, y * 40 + 25, x * 40 + 55, y * 40 + 55, fill='white')
        elif A[y][x] == 2:
            w1.create_oval(x * 40 + 25, y * 40 + 25, x * 40 + 55, y * 40 + 55, fill='black')
    for x, y in possible_location_dic.keys():
        w1.create_text(x * 40 + 40, y * 40 + 40, text='+', font=('华文隶书', 20))

def judge(alist):
    # 长度为1，则返回False
    if len(alist) == 1:
        return []
    # 查找元素下标
    try:
        sec_index = alist[1:].index(alist[0]) + 1
        for i in range(1, sec_index):
            if alist[i] == alist[0] or alist[i] == 0:
                return []
        return [i for i in range(1, sec_index)]
    except:
        # 查不到第二个元素，则返回False
        return []

def if_good(x, y, if_black):
    global A
    good_location = []

    # 向左
    alist = [A[y][i] for i in range(x, -1, -1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y, x - i] for i in good_list]

    # 向右
    alist = [A[y][i] for i in range(x, 8)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y, x + i] for i in good_list]

    # 向上
    alist = [A[i][x] for i in range(y, -1, -1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y - i, x] for i in good_list]

    # 向下
    alist = [A[i][x] for i in range(y, 8)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y + i, x] for i in good_list]

    # 向左上
    alist = [A[y - i][x - i] for i in range(0, min([x, y]) + 1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y - i, x - i] for i in good_list]

    # 向右上
    alist = [A[y - i][x + i] for i in range(0, min([7 - x, y]) + 1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y - i, x + i] for i in good_list]

    # 向左下
    alist = [A[y + i][x - i] for i in range(0, min([x, 7 - y]) + 1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y + i, x - i] for i in good_list]

    # 向右下
    alist = [A[y + i][x + i] for i in range(0, min([7 - x, 7 - y]) + 1)]
    # 第一个位置的调整
    alist[0] = 2 if if_black else 1
    good_list = judge(alist)
    good_location = good_location + [[y + i, x + i] for i in good_list]

    return good_location

# 寻找可以放的棋子的位置
def get_possible_location(if_black):
    xylist = [(i, j) for j in range(0, 8) for i in range(0, 8)]
    good_location_dic = {}
    for x, y in xylist:
        if A[y][x] != 0:
            continue
        good_location = if_good(x, y, if_black)
        if len(good_location) > 0:
            good_location_dic[(x, y)] = good_location
    return good_location_dic

# 中间夹着的棋子颜色翻转
def change_chess(x, y, if_black):
    global A
    for i in now_location_dic[(x, y)]:
        A[i[0]][i[1]] = 2 if if_black else 1

# 人机
def computer():
    global now_location_dic, if_black, A
    length_dic = dict(zip([i for i in list(now_location_dic.keys())], [len(now_location_dic[i]) for i in list(now_location_dic.keys())]))
    max_length = max(length_dic.values())
    max_length_list = list(filter(lambda x: length_dic[x]==max_length, list(length_dic.keys())))
    rand_p = max_length_list[random.randint(0, len(max_length_list) - 1)]
    y = rand_p[1]
    x = rand_p[0]
    computer_step(x, y)

def computer_step(x, y):
    global A, if_black, now_location_dic, last_A
    while (x, y) in now_location_dic.keys():
        last_A = A.copy()
        if if_black:
            A[y][x] = 2
            change_chess(x, y, if_black)
            if_black = False
        else:
            A[y][x] = 1
            change_chess(x, y, if_black)
            if_black = True

        possible_location_dic = get_possible_location(if_black)
        now_location_dic = possible_location_dic
        draw_chess(possible_location_dic)
        print(if_black, now_location_dic)

        # 如果是没位置可下了，就轮空
        if len(now_location_dic) == 0:
            if_black = not if_black

        if len(get_possible_location(if_black)) == 0 and len(get_possible_location(not if_black)) == 0:
            w_cnt = A[A == 1].sum()
            b_cnt = int(A[A == 2].sum() / 2)
            if w_cnt > b_cnt:
                tkinter.messagebox.showinfo('提示', '白棋获胜')
            elif w_cnt < b_cnt:
                tkinter.messagebox.showinfo('提示', '黑棋获胜')
            else:
                tkinter.messagebox.showinfo('提示', '平局')
        cal()

# 下棋的动作
def callback(event):
    global A, if_black, now_location_dic, last_A
    x = (event.x - 20) // 40
    y = (event.y - 20) // 40

    while (x, y) in now_location_dic.keys():
        last_A = A.copy()
        if if_black:
            A[y][x] = 2
            change_chess(x, y, if_black)
            if_black = False
        else:
            A[y][x] = 1
            change_chess(x, y, if_black)
            if_black = True

        possible_location_dic = get_possible_location(if_black)
        now_location_dic = possible_location_dic
        draw_chess(possible_location_dic)
        print(if_black, now_location_dic)

        # 如果是没位置可下了，就轮空
        if len(now_location_dic) == 0:
            if_black = not if_black

        if len(get_possible_location(if_black)) == 0 and len(get_possible_location(not if_black)) == 0:
            w_cnt = A[A == 1].sum()
            b_cnt = int(A[A == 2].sum() / 2)
            if w_cnt > b_cnt:
                tkinter.messagebox.showinfo('提示', '白棋获胜')
            elif w_cnt < b_cnt:
                tkinter.messagebox.showinfo('提示', '黑棋获胜')
            else:
                tkinter.messagebox.showinfo('提示', '平局')
        cal()
        computer()

possible_location_dic = get_possible_location(if_black)
now_location_dic = possible_location_dic
draw_chess(possible_location_dic)
# print(if_black, now_location_dic)
w1.bind("<Button -1>", callback)
w1.pack()
mainloop()

# if_good(5, 3, True)