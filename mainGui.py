import tkinter as tk
from tkinter import messagebox
bd = [" "]*9
pl = "X"
ai = "O"
root = tk.Tk()
root.title("TicTacToe")
btns = []
def chk(b):
    w = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a,c,d in w:
        if b[a]==b[c]==b[d] and b[a]!=" ":
            return b[a]
    if " " not in b:
        return "d"
    return None
def emp(b):
    return [i for i,v in enumerate(b) if v==" "]
def mm(b,t,ai_s,hu_s,d=0):
    r = chk(b)
    if r==ai_s:
        return {"s":10-d}
    if r==hu_s:
        return {"s":d-10}
    if r=="d":
        return {"s":0}
    mvlist=[]
    for i in emp(b):
        b[i]=t
        nx = hu_s if t==ai_s else ai_s
        rr = mm(b,nx,ai_s,hu_s,d+1)
        mvlist.append({"i":i,"s":rr["s"]})
        b[i]=" "
    if t==ai_s:
        best = mvlist[0]
        for m in mvlist:
            if m["s"]>best["s"]:
                best=m
        return best
    else:
        best = mvlist[0]
        for m in mvlist:
            if m["s"]<best["s"]:
                best=m
        return best
def ai_do():
    e = emp(bd)
    if not e:
        return
    if len(e)==9:
        bd[4]=ai
        upd(4)
        return
    m = mm(bd,ai,ai,pl)
    i = m["i"]
    bd[i]=ai
    upd(i)
def upd(i):
    btns[i]["text"]=bd[i]
    btns[i]["state"]="disabled"
def human(i):
    if bd[i]!=" ":
        return
    bd[i]=pl
    upd(i)
    r = chk(bd)
    if r:
        end(r)
        return
    root.after(150,ai_turn)
def ai_turn():
    ai_do()
    r = chk(bd)
    if r:
        end(r)
def end(r):
    for b in btns:
        b["state"]="disabled"
    if r=="d":
        messagebox.showinfo("over","Draw")
    elif r==pl:
        messagebox.showinfo("over","You win")
    else:
        messagebox.showinfo("over","AI wins")
def rst():
    global bd
    bd=[" "]*9
    for b in btns:
        b["text"]=" "
        b["state"]="normal"
f = tk.Frame(root); f.pack(padx=8,pady=8)
for i in range(9):
    b = tk.Button(f,text=" ",width=5,height=2,font=("Arial",22),command=lambda i=i: human(i))
    b.grid(row=i//3,column=i%3,padx=2,pady=2)
    btns.append(b)
bot = tk.Frame(root); bot.pack(pady=6)
tk.Button(bot,text="Restart",command=rst).pack(side="left",padx=5)
tk.Button(bot,text="Play as O (AI first)",command=lambda: choose("O")).pack(side="left",padx=5)
tk.Button(bot,text="Play as X (You first)",command=lambda: choose("X")).pack(side="left",padx=5)
def choose(s):
    global pl,ai
    pl=s
    ai="O" if pl=="X" else "X"
    rst()
    if pl==ai:
        pass
    if pl=="O":
        root.after(200,ai_turn)
root.mainloop()