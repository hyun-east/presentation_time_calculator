import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
k = 1
def bt2cmd():
    script = txt.get("1.0",END)
    def syl(x):
        x = x.replace("q", "e")
        x = x.replace("w", "e")
        x = x.replace("e", "e")
        x = x.replace("r", "e")
        x = x.replace("t", "e")
        x = x.replace("y", "e")
        x = x.replace("u", "e")
        x = x.replace("i", "e")
        x = x.replace("o", "e")
        x = x.replace("p", "e")
        x = x.replace("a", "e")
        x = x.replace("s", "e")
        x = x.replace("d", "e")
        x = x.replace("f", "e")
        x = x.replace("g", "e")
        x = x.replace("h", "e")
        x = x.replace("j", "e")
        x = x.replace("k", "e")
        x = x.replace("l", "e")
        x = x.replace("z", "e")
        x = x.replace("x", "e")
        x = x.replace("c", "e")
        x = x.replace("v", "e")
        x = x.replace("b", "e")
        x = x.replace("n", "e")
        x = x.replace("m", "e")
        x = x.replace("Q", "e")
        x = x.replace("W", "e")
        x = x.replace("E", "e")
        x = x.replace("R", "e")
        x = x.replace("T", "e")
        x = x.replace("Y", "e")
        x = x.replace("U", "e")
        x = x.replace("I", "e")
        x = x.replace("O", "e")
        x = x.replace("P", "e")
        x = x.replace("A", "e")
        x = x.replace("S", "e")
        x = x.replace("D", "e")
        x = x.replace("F", "e")
        x = x.replace("G", "e")
        x = x.replace("H", "e")
        x = x.replace("J", "e")
        x = x.replace("K", "e")
        x = x.replace("L", "e")
        x = x.replace("Z", "e")
        x = x.replace("X", "e")
        x = x.replace("C", "e")
        x = x.replace("V", "e")
        x = x.replace("B", "e")
        x = x.replace("N", "e")
        x = x.replace("M", "e")
        result = x.count("e")
        return(result)
    def cnt(x):
        result = x.count(" ")
        return(result)
    def klen(x):
        result = len(x) - cnt(x)
        return(result)
    def stc(x):
        result = x.count(".") + x.count("?") + x.count("!")
        return(result)
    j = 0
    while j == 0:
        j = j+1
        if k == 1:

            print("%d 단어\n%d 음절" % (w_seg, lenr))
            print("약 %02d분 %02d초" %(time_m, time_s))
            msgbox.showinfo("결과","%d 단어\n%d 음절\n약 %02d분 %02d초" % (w_seg, lenr, time_m, time_s))


def bt3cmd():
    txt.delete("1.0",END)
root = Tk()
root.title("발표 시간 측정기")
root.geometry("960x590")
txt = Text(root,width=147, height = 40)
txt.pack()
btn2 = Button(root,padx = 499, pady = 5, text = "계산", command = bt2cmd)
btn2.pack()
btn3 = Button(root,padx = 493, pady = 5, text = "지우기", command = bt3cmd)
btn3.pack()
root.mainloop()


