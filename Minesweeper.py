from tkinter import *
from random import *
from tkinter import messagebox
#import mysql.connector as msq

def main_window():
    global ms,ne,etv
    ms = Tk()
    ms.configure(background='light green')
    nl = Label(ms,text='NAME').grid(row=1,columnspan=1)
    etv = StringVar()
    ne = Entry(ms,textvariable=etv)
    ne.grid(row=1,column=2,columnspan=2)
    sb = Button(ms,text='START',width=15,bg='yellow',command=start).grid(row=2,column=2)
    ib = Button(ms,text='INSTRUCTIONS',width=15,bg='yellow',command=instruction).grid(row=3,column=2)
    eb = Button(ms,text='EXIT',width=15,bg='yellow',command=closeit).grid(row=4,column=2)

def start():
    global sw,bl
    sw = Tk()
    sw.title('MINESWEEPER')
    bl = []
    buttons()

def instruction():
    iw = Tk()
    iw.geometry('700x150')
    iw.title('INSTRUCTIONS')
    i = Text(iw)
    i.pack()
    i.insert(END,'\t Welcome to Minesweeper!!\nRules:\
        \n1. The objective of the game is to clear a rectangular board containing hidden "mines" without detonating any of them\
        \n2. The numbers on the board represent how many bombs are adjacent to a square\
        \n3. Grid : 6 x 6 \t Bombs : 6')
    
def closeit():
    ms.destroy()

def buttons():
    global ro,col,bts,pos
    for ro in range(6):
        for col in range(6):
            pos = ro * 6 + col
            bts = Button(sw,text='-',height=2,width=5,bg='light blue',command=lambda pos=pos,ro=ro,col=col:btncommand(pos,ro,col))
            bts.grid(row=ro,column=col) 
            bl.append(bts)

def btncommand(ind,x,y):
    global score
    bl[ind]['text'] = str(board[x][y])
    if (bl[ind]['text'] == str(board[x][y])) and (bl[ind]['text'] != '*'):
        score += 1
        bl[ind]['state'] = DISABLED
        winner()
    try:
        if bl[ind]['text'] == '*':
            gameover()
    except TclError:
        pass
    
def winner():
    global score,res
    if score == 30:
        messagebox.showinfo("GAME OVER",f'YOU ARE WINNER!\nYOUR SCORE IS {str(score)}')
        res = 'WIN'
        sw.destroy()

def gameover():
    global score,res
    messagebox.showinfo('GAME OVER',f'YOU LOST!\nYOUR SCORE IS {str(score)}')
    res = 'LOST'
    sw.destroy()

score = 0
board = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],
[0,0,0,0,0,0],[0,0,0,0,0,0]]
col_list = [1,2,3,4]
for r in range(6):    
    co = choice(col_list)
    board[r][co] = '*'        
    if r!=5:
        board[r][co+1] += 1
        board[r][co-1] += 1
        board[r+1][co+1] += 1
        board[r+1][co] += 1
        board[r+1][co-1] += 1
    if r==5:
        board[r][co+1] += 1
        board[r][co-1] += 1
        if board[r-1][co] != '*':
            board[r-1][co] += 1
        if board[r-1][co-1] != '*':
            board[r-1][co-1] += 1
        if board[r-1][co+1] != '*':
            board[r-1][co+1] += 1
    if (r>0 and r<5):
        if board[r-1][co] != '*':
            board[r-1][co] += 1
        if board[r-1][co-1] != '*':
            board[r-1][co-1] += 1
        if board[r-1][co+1] != '*':
            board[r-1][co+1] += 1

def msg():
    main_window()
    ms.mainloop()

if __name__ == '__main__':
    main_window()
    ms.mainloop()
    '''name = etv.get()
    con = msq.connect(host='localhost',user='root',passwd='Pranavpk6')#123
    cur = con.cursor()
    #cmd0 = cur.execute('CREATE DATABASE Minesweeper')
    cmd1 = cur.execute('USE Minesweeper')
    #cmd2 = cur.execute('CREATE TABLE MineData(Player_Name VARCHAR(30),Score INT,Result CHAR(4))')
    cmd3 = 'INSERT INTO MineData VALUES(%s,%s,%s)'
    cmd4 = (name,str(score),res)
    cmd5 = cur.execute(cmd3,cmd4)
    con.commit()
    con.close()'''   
