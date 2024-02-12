import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
def btcmd():
    global k
    k = 2
    lan = combobox.get()
    if lan == "한국어":
        k = 0
        print("한국어")
    if lan == "영어":
        k = 1
        print("영어")
    elif lan == "언어를 선택하신 후 아래 \'선택\' 버튼을 눌러주십시오.":
        msgbox.showerror("오류", "언어를 고르신 후 선택버튼을 눌러주십시오")
def bt2cmd():
    script = txt.get("1.0",END)
    def syl(x):
        x = x.replace("a", "e")
        x = x.replace("o", "e")
        x = x.replace("u", "e")
        x = x.replace("i", "e")
        x = x.replace("y", "e")
        x = x.replace("A", "e")
        x = x.replace("O", "e")
        x = x.replace("U", "e")
        x = x.replace("I", "e")
        x = x.replace("Y", "e")
        x = x.replace("E", "e")
        for i in range(3):
            x = x.replace("ee", "e")
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
        if k == 0:
            w_seg = cnt(script) +1
            syll = syl(script) + 1
            lenr = klen(script)
            time = lenr*(0.2) + stc(script) * (0.1) + syll * (0.24)
            time_m = time // 60
            time_s = time % 60
            print("%d 단어\n%d 음절" % (w_seg, lenr))
            print("약 %02d분 %02d초" %(time_m, time_s))
            msgbox.showinfo("결과","%d 단어\n%d 음절\n약 %02d분 %02d초" % (w_seg, lenr, time_m, time_s))
        elif k==1:
            w_seg = cnt(script) +1 # 띄어쓰기 개수(어절 개수)
            syll = syl(script) + 1  # 음절 개수
            lenr = klen(script)
            avg_syll = syll / w_seg
            time = lenr*(0.2) + syll * (0.24)+ stc(script) * (0.1)
            time_m = time // 60
            time_s = time % 60
            print("%d 어절\n약 %d 음절\n평균 약 %f음절" % (w_seg, syll, avg_syll))
            print("약 %02d분 %02d초" % (time_m, time_s))
            msgbox.showinfo("결과","%d 어절\n약 %d 음절\n평균 약 %f음절\n약 %02d분 %02d초"% (w_seg, syll, avg_syll, time_m, time_s))

def bt3cmd():
    txt.delete("1.0",END)
root = Tk()
root.title("발표 시간 측정기")
root.geometry("960x647")
combobox = ttk.Combobox(root,width = 144, height = 5, values=["한국어", "영어"])
combobox.pack()
combobox.set("한국어")
btcmd()
btn = Button(root,padx = 499, pady = 5, text = "선택", command = btcmd)
btn.pack()
txt = Text(root,width=147, height = 40)
txt.pack()
btn2 = Button(root,padx = 499, pady = 5, text = "계산", command = bt2cmd)
btn2.pack()
btn3 = Button(root,padx = 493, pady = 5, text = "지우기", command = bt3cmd)
btn3.pack()
root.mainloop()


