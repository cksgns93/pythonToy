import tkinter as tk
from tkinter import *
from tkinter import messagebox
import openpyxl
import operator

window = tk.Tk()
window.title(" DISC 성격 검사 ")


#변수

achoice1 = IntVar()
bchoice1 = IntVar()
cchoice1 = IntVar()
dchoice1 = IntVar()
echoice1 = IntVar()
fchoice1 = IntVar()
gchoice1 = IntVar()
hchoice1 = IntVar()
ichoice1 = IntVar()
jchoice1 = IntVar()
kchoice1 = IntVar()
lchoice1 = IntVar()
mchoice1 = IntVar()
nchoice1 = IntVar()
ochoice1 = IntVar()
pchoice1 = IntVar()
qchoice1 = IntVar()
rchoice1 = IntVar()
schoice1 = IntVar()
tchoice1 = IntVar()
uchoice1 = IntVar()
vchoice1 = IntVar()
wchoice1 = IntVar()
xchoice1 = IntVar()
ychoice1 = IntVar()
zchoice1 = IntVar()
Achoice1 = IntVar()
Bchoice1 = IntVar()

achoice2 = IntVar()
bchoice2 = IntVar()
cchoice2 = IntVar()
dchoice2 = IntVar()
echoice2 = IntVar()
fchoice2 = IntVar()
gchoice2 = IntVar()
hchoice2 = IntVar()
ichoice2 = IntVar()
jchoice2 = IntVar()
kchoice2 = IntVar()
lchoice2 = IntVar()
mchoice2 = IntVar()
nchoice2 = IntVar()
ochoice2 = IntVar()
pchoice2 = IntVar()
qchoice2 = IntVar()
rchoice2 = IntVar()
schoice2 = IntVar()
tchoice2 = IntVar()
uchoice2 = IntVar()
vchoice2 = IntVar()
wchoice2 = IntVar()
xchoice2 = IntVar()
ychoice2 = IntVar()
zchoice2 = IntVar()
Achoice2 = IntVar()
Bchoice2 = IntVar()

c1 = [achoice1, bchoice1, cchoice1, dchoice1, echoice1, fchoice1, gchoice1, hchoice1, ichoice1, jchoice1, kchoice1, lchoice1, mchoice1, nchoice1, ochoice1, pchoice1, qchoice1, rchoice1, schoice1, tchoice1, uchoice1, vchoice1, wchoice1, xchoice1, ychoice1, zchoice1, Achoice1, Bchoice1]
c2 = [achoice2, bchoice2, cchoice2, dchoice2, echoice2, fchoice2, gchoice2, hchoice2, ichoice2, jchoice2, kchoice2, lchoice2, mchoice2, nchoice2, ochoice2, pchoice2, qchoice2, rchoice2, schoice2, tchoice2, uchoice2, vchoice2, wchoice2, xchoice2, ychoice2, zchoice2, Achoice2, Bchoice2]   




#함수
def exitfn():

    exmsgbox = tk.messagebox.askquestion("종료", "검사를 종료하시겠습니까?")

    if exmsgbox == "yes":
        
        window.destroy()

def resultcheck():
    a = 1
    b = 1
    
    for i in c1:
        
        a = a*i.get()

    for i in c2:

        b = b*i.get()

    if a == 0 or b == 0:
            chmsgbox = tk.messagebox.showinfo("오류", "선택하지 않은 항목이 있습니다.")

    else:
        msgbox = tk.messagebox.askquestion("검사 완료", "검사가 정상적으로 완료되었습니다.\n결과를 확인하시겠습니까?")
            
        if msgbox == "yes":
                
            exam()

    
def exam():
    
    DM = 0
    IM = 0
    SM = 0
    CM = 0
    NM = 0

    Dm = 0
    Im = 0
    Sm = 0
    Cm = 0
    Nm = 0

    D = 0
    I = 0
    S = 0
    C = 0
    
    for i in c1:
        
        if i.get() == 1:
            DM = DM + i.get()
            
        elif i.get() == 2:
            IM = IM + i.get()/2

        elif i.get() == 3:
            SM = SM + i.get()/3

        elif i.get() == 4:
            CM = CM + i.get()/4

        elif i.get() == 5:
            NM = NM + i.get()/5

        else:
            NM = NM + i.get()/6

    for i in c2:
        if i.get() == 1:
            Dm = Dm + i.get()
            
        elif i.get() == 2:
            Im = Im + i.get()/2

        elif i.get() == 3:
            Sm = Sm + i.get()/3

        elif i.get() == 4:
            Cm = Cm + i.get()/4

        elif i.get() == 5:
            Nm = Nm + i.get()/5

        else:
            NM = NM + i.get()/6

    DF = DM - Dm
    IF = IM - Im
    SF = SM - Sm
    CF = CM - Cm
    
    if DF >= 6 and DF <= 28:
        D = 7
    elif DF <= 5 and DF >= 0:
        D = 6
    elif DF <= -1 and DF >= -4:
        D = 5
    elif DF <= -5 and DF >= -7:
        D = 4
    elif DF <= -8 and DF >= -11:
        D = 3
    elif DF <= -12 and DF >= -14:
        D = 2
    else:
        D = 1
        
    if IF <= 28 and IF >= 8:
        I = 7
    elif IF <= 7 and IF >= 6:
        I = 6
    elif IF <= 5 and IF >= 3:
        I = 5
    elif IF <= 2 and IF >= 1:
        I = 4
    elif IF <= 0 and IF >= -2:
        I = 3
    elif IF <= -3 and IF >= -5:
        I = 2
    else:
        I = 1

    if SF <= 28 and SF >= 12:
        S = 7
    elif SF <= 1 and SF >= 9:
        S = 6
    elif SF <= 8 and SF >= 6:
        S = 5
    elif SF <= 5 and SF >= 3:
        S = 4
    elif SF <= 2 and SF >= 0:
        S = 3
    elif SF <= -1 and SF >= -4:
        S = 2
    else:
        S = 1

    if CF <= 28 and CF >= 6:
        C = 7
    elif CF <= 5 and CF >= 3:
        C = 6
    elif CF <= 2 and CF >= 0:
        C = 5
    elif CF <= -1 and CF >= -2:
        C = 4
    elif CF <= -3 and CF >= -5:
        C = 3
    elif CF <= -4 and CF >= -8:
        C = 2
    else:
        C = 1

    DISC = D*1000 + I*100 + S*10 + C
    
    file = openpyxl.load_workbook("DISC.xlsx")
    sheet = file.active

    for i in sheet.rows:
        if (operator.eq(i[0].value, DISC)):
            DISCY = i[1].value


#해설지 윈도우
    window2 = tk.Tk()
    window2.title(" DISC 검사 결과 ")

    def retryfn():

        window2.destroy()

    def exit2fn():
        exmsgbox2 = tk.messagebox.askquestion("종료", "검사를 종료하시겠습니까?")

        if exmsgbox2 == "yes":
            
            window2.destroy()
            window.destroy()

    Label(window2, text = "DISC 수치").grid(row = 0 , column = 0)
    Label(window2, text = D).grid(row = 0 , column = 1)
    Label(window2, text = I).grid(row = 0 , column = 2)
    Label(window2, text = S).grid(row = 0 , column = 3)
    Label(window2, text = C).grid(row = 0 , column = 4)
    Label(window2, text = DISCY).grid(row = 0 , column = 5)
    Label(window2, text = "입니다.").grid(row = 0 , column = 6)
    
    for i in sheet.rows:
        if (operator.eq(i[3].value, DISCY)):
                Label(window2, text = "정서 :").grid(row = 1 , column = 7, sticky = E)
                Label(window2, text = "목표 :").grid(row = 2 , column = 7, sticky = E)
                Label(window2, text = "타인을 판단하는 기준 :").grid(row = 3 , column = 7, sticky = E)
                Label(window2, text = "타인에게 영향을 주는 점 :").grid(row = 4 , column = 7, sticky = E)
                Label(window2, text = "조직에의 공헌 :").grid(row = 5 , column = 7, sticky = E)
                Label(window2, text = "지나친 점 :").grid(row = 6 , column = 7, sticky = E)
                Label(window2, text = "압력 아래서 :").grid(row = 7 , column = 7, sticky = E)
                Label(window2, text = "두려움 :").grid(row = 8 , column = 7, sticky = E)
                Label(window2, text = "효과증진책 :").grid(row = 9 , column = 7, sticky = E)
                Label(window2, text = " ").grid(row = 10 , column = 7, sticky = E)
                Label(window2, text = "총평 : ").grid(row = 11 , column = 7, sticky = E)
                
                Label(window2, text = i[4].value).grid(row = 1 , column = 8, sticky = W)
                Label(window2, text = i[5].value).grid(row = 2 , column = 8, sticky = W)
                Label(window2, text = i[6].value).grid(row = 3 , column = 8, sticky = W)
                Label(window2, text = i[7].value).grid(row = 4 , column = 8, sticky = W)
                Label(window2, text = i[8].value).grid(row = 5 , column = 8, sticky = W)
                Label(window2, text = i[9].value).grid(row = 6 , column = 8, sticky = W)
                Label(window2, text = i[10].value).grid(row = 7 , column = 8, sticky = W)
                Label(window2, text = i[11].value).grid(row = 8 , column = 8, sticky = W)
                Label(window2, text = i[12].value).grid(row = 9 , column = 8, sticky = W)
                Label(window2, text = i[13].value, justify = "left").grid(row = 11 , column = 8, sticky = W)
    

    #다시하기 버튼
    Button(window2, text = "다시하기", command = retryfn).grid(row = 12, column = 8)

    #종료 버튼
    Button(window2, text = "종료", command = exit2fn).grid(row = 12, column = 10)


#질문지 작성



#1번 질문

al = [("열정적인", 2, 1),("과감한", 1, 2),("치밀한", 4, 3),("만족해 하는", 3, 4)]
Label(window, text = "1.").grid(row = 0, column = 0)

Label(window, text = "최고").grid(row = 1, column = 0, sticky = W, padx = 5)

for txt, val, loc in al:
    Radiobutton(window,text=txt, variable=achoice1, value=val).grid(row = loc + 1, column = 0, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 1, sticky = W)

for txt, val, loc in al:
    Radiobutton(window, variable=achoice2, value=val).grid(row = loc + 1, column = 1, sticky = W)


#2번 질문
bl1 = [("조심성 있는", 4, 1),("결단력 있는", 1, 2),("확신을 주는", 2, 3),("온화한", 3, 4)]
bl2 = [("조심성 있는", 4, 1),("결단력 있는", 1, 2),("확신을 주는", 2, 3),("온화한", 5, 4)]
Label(window, text = "2.").grid(row = 6, column = 0)

Label(window, text = "최고").grid(row = 7, column = 0, sticky = W, padx = 5)

for txt, val, loc in bl1:
    n = Radiobutton(window,text=txt, variable=bchoice1, value=val).grid(row = loc + 7, column = 0, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 1, sticky = W)

for txt, val, loc in bl2:
    n = Radiobutton(window, variable=bchoice2, value=val).grid(row = loc + 7, column = 1, sticky = W)



#3번 질문
cl1 = [("다정한", 2, 1),("정확한", 4, 2),("솔직하게 말하는", 1,3),("조용한", 5, 4)]
cl2 = [("다정한", 2, 1),("정확한", 4, 2),("솔직하게 말하는", 1,3),("조용한", 3, 4)]
Label(window, text = "3.").grid(row = 12, column = 0)

Label(window, text = "최고").grid(row = 13, column = 0, sticky = W, padx = 5)

for txt, val, loc in cl1:
    Radiobutton(window,text=txt, variable=cchoice1, value=val).grid(row = loc + 13, column = 0, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 1, sticky = W)

for txt, val, loc in cl2:
    Radiobutton(window, variable=cchoice2, value=val).grid(row = loc + 13, column = 1, sticky = W)




#4번 질문
dl = [("말하기를 좋아하는", 2, 1),("자제력 있는", 4, 2),("관습을 따르는", 3, 3),("쉽게 결론 내리는", 1, 4)]
Label(window, text = "4.").grid(row = 18, column = 0)

Label(window, text = "최고").grid(row = 19, column = 0, sticky = W, padx = 5)

for txt, val, loc in dl:
    Radiobutton(window,text=txt, variable=dchoice1, value=val).grid(row = loc + 19, column = 0, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 19, column = 1, sticky = W)

for txt, val, loc in dl:
    Radiobutton(window, variable=dchoice2, value=val).grid(row = loc + 19, column = 1, sticky = W)




#5번 질문
el = [("도전하는", 1, 1),("통찰력 있는", 4, 2),("사교성 있는", 2, 3),("온순한", 3, 4)]
Label(window, text = "5.").grid(row = 24, column = 0)

Label(window, text = "최고").grid(row = 25, column = 0, sticky = W, padx = 5)

for txt, val, loc in el:
    Radiobutton(window,text=txt, variable=echoice1, value=val).grid(row = loc + 25, column = 0, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 25, column = 1, sticky = W)

for txt, val, loc in el:
    Radiobutton(window, variable=echoice2, value=val).grid(row = loc + 25, column = 1, sticky = W)



#6번 질문
fl1 = [("부드러운", 3, 1),("설득력 있는", 2, 2),("겸손한", 5, 3),("독창적인", 6, 4)]
fl2 = [("부드러운", 3, 1),("설득력 있는", 2, 2),("겸손한", 4, 3),("독창적인", 1, 4)]
Label(window, text = "6.").grid(row = 0, column = 2)

Label(window, text = "최고").grid(row = 1, column = 2, sticky = W, padx = 5)

for txt, val, loc in fl1:
    Radiobutton(window,text=txt, variable=fchoice1, value=val).grid(row = loc + 1, column = 2, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 3, sticky = W)

for txt, val, loc in fl2:
    Radiobutton(window, variable=fchoice2, value=val).grid(row = loc + 1, column = 3, sticky = W)


#7번 질문
gl1 = [("표현력 있는", 2, 1),("신중한", 4, 2),("주도적인", 1, 3),("잘 받아들이는", 5, 4)]
gl2 = [("표현력 있는", 2, 1),("신중한", 4, 2),("주도적인", 1, 3),("잘 받아들이는", 3, 4)]
Label(window, text = "7.").grid(row = 6, column = 2)

Label(window, text = "최고").grid(row = 7, column = 2, sticky = W, padx = 5)

for txt, val, loc in gl1:
    Radiobutton(window,text=txt, variable=gchoice1, value=val).grid(row = loc + 7, column = 2, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 3, sticky = W)

for txt, val, loc in gl2:
    Radiobutton(window, variable=gchoice2, value=val).grid(row = loc + 7, column = 3, sticky = W)



#8번 질문
hl1 = [("긍정적인", 2, 1),("세심하게 살피는", 4, 2),("온건한", 3, 3),("참을성이 적은", 1, 4)]
hl2 = [("긍정적인", 2, 1),("세심하게 살피는", 5, 2),("온건한", 3, 3),("참을성이 적은", 1, 4)]
Label(window, text = "8.").grid(row = 12, column = 2)

Label(window, text = "최고").grid(row = 13, column = 2, sticky = W, padx = 5)

for txt, val, loc in hl1:
    Radiobutton(window,text=txt, variable=hchoice1, value=val).grid(row = loc + 13, column = 2, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 3, sticky = W)

for txt, val, loc in hl2:
    Radiobutton(window, variable=hchoice2, value=val).grid(row = loc + 13, column = 3, sticky = W)


#9번 질문
il = [("사려 깊은", 4, 1),("남 의견에 잘 동의하는", 3, 2),("사람들에게 호감을 주는", 2, 3),("자기 주장이 강한", 1, 4)]
Label(window, text = "9.").grid(row = 18, column = 2)

Label(window, text = "최고").grid(row = 19, column = 2, sticky = W, padx = 5)

for txt, val, loc in il:
    Radiobutton(window,text=txt, variable=ichoice1, value=val).grid(row = loc + 19, column = 2, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 19, column = 3, sticky = W)

for txt, val, loc in il:
    Radiobutton(window, variable=ichoice2, value=val).grid(row = loc + 19, column = 3, sticky = W)



#10번 질문
jl1 = [("용감한", 1, 1),("격려하는", 2, 2),("순응하는", 3, 3),("수줍어하는", 5, 4)]
jl2 = [("용감한", 1, 1),("격려하는", 2, 2),("순응하는", 3, 3),("수줍어하는", 4, 4)]
Label(window, text = "10.").grid(row = 24, column = 2)

Label(window, text = "최고").grid(row = 25, column = 2, sticky = W, padx = 5)

for txt, val, loc in jl1:
    Radiobutton(window,text=txt, variable=jchoice1, value=val).grid(row = loc + 25, column = 2, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 25, column = 3, sticky = W)

for txt, val, loc in jl2:
    Radiobutton(window, variable=jchoice2, value=val).grid(row = loc + 25, column = 3, sticky = W)


#11번 질문
kl = [("말이 적은", 4, 1),("호의적인", 3, 2),("의지가 강한", 1, 3),("명랑한", 2, 4)]
Label(window, text = "11.").grid(row = 0, column = 4)

Label(window, text = "최고").grid(row = 1, column = 4, sticky = W, padx = 5)

for txt, val, loc in kl:
    Radiobutton(window,text=txt, variable=kchoice1, value=val).grid(row = loc + 1, column = 4, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 5, sticky = W)

for txt, val, loc in kl:
    Radiobutton(window, variable=kchoice2, value=val).grid(row = loc + 1, column = 5, sticky = W)


#12번 질문
ll = [("남을 격려하는", 2, 1),("친절한", 3, 2),("분별력 있는", 4, 3),("독립심이 강한", 1, 4)]
Label(window, text = "12.").grid(row = 6, column = 4)

Label(window, text = "최고").grid(row = 7, column = 4, sticky = W, padx = 5)

for txt, val, loc in ll:
    Radiobutton(window,text=txt, variable=lchoice1, value=val).grid(row = loc + 7, column = 4, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 5, sticky = W)

for txt, val, loc in ll:
    Radiobutton(window, variable=lchoice2, value=val).grid(row = loc + 7, column = 5, sticky = W)


#13번 질문
ml = [("경쟁심이 있는", 1, 1),("이해심 있는", 3, 2),("즐거운", 2, 3),("자신을 잘 드러내지 않는", 4, 4)]
Label(window, text = "13.").grid(row = 12, column = 4)

Label(window, text = "최고").grid(row = 13, column = 4, sticky = W, padx = 5)

for txt, val, loc in ml:
    Radiobutton(window,text=txt, variable=mchoice1, value=val).grid(row = loc + 13, column = 4, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 5, sticky = W)

for txt, val, loc in ml:
    Radiobutton(window, variable=mchoice2, value=val).grid(row = loc + 13, column = 5, sticky = W)


#14번 질문
nl = [("기준이 높은", 4, 1),("유순한", 3, 2),("확고한", 1, 3),("쾌활한", 2, 4)]
Label(window, text = "14.").grid(row = 18, column = 4)

Label(window, text = "최고").grid(row = 19, column = 4, sticky = W, padx = 5)

for txt, val, loc in nl:
    Radiobutton(window,text=txt, variable=nchoice1, value=val).grid(row = loc + 19, column = 4, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 19, column = 5, sticky = W)

for txt, val, loc in nl:
    Radiobutton(window, variable=nchoice2, value=val).grid(row = loc + 19, column = 5, sticky = W)



#15번 질문
ol1 = [("매력적인", 2, 1),("생각이 깊은", 4, 2),("의지가 굳은", 1, 3),("일관되게 행동하는", 3, 4)]
ol2 = [("매력적인", 2, 1),("생각이 깊은", 5, 2),("의지가 굳은", 1, 3),("일관되게 행동하는", 3, 4)]
Label(window, text = "15.").grid(row = 24, column = 4)

Label(window, text = "최고").grid(row = 25, column = 4, sticky = W, padx = 5)

for txt, val, loc in ol1:
    Radiobutton(window,text=txt, variable=ochoice1, value=val).grid(row = loc + 25, column = 4, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 25, column = 5, sticky = W)

for txt, val, loc in ol2:
    Radiobutton(window, variable=ochoice2, value=val).grid(row = loc + 25, column = 5, sticky = W)


#16번 질문
pl = [("논리적인", 4, 1),("대담한", 1, 2),("충실한", 3, 3),("인기 있는", 2, 4)]
Label(window, text = "16.").grid(row = 0, column = 6)

Label(window, text = "최고").grid(row = 1, column = 6, sticky = W, padx = 5)

for txt, val, loc in pl:
    Radiobutton(window,text=txt, variable=pchoice1, value=val).grid(row = loc + 1, column = 6, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 7, sticky = W)

for txt, val, loc in pl:
    Radiobutton(window, variable=pchoice2, value=val).grid(row = loc + 1, column = 7, sticky = W)


#17번 질문
ql = [("사교적인", 2, 1),("참을성 있는", 3, 2),("자신감 있는", 1, 3),("점잖게 말하는", 4, 4)]
Label(window, text = "17.").grid(row = 6, column = 6)

Label(window, text = "최고").grid(row = 7, column = 6, sticky = W, padx = 5)

for txt, val, loc in ql:
    Radiobutton(window,text=txt, variable=qchoice1, value=val).grid(row = loc + 7, column = 6, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 7, sticky = W)

for txt, val, loc in ql:
    Radiobutton(window, variable=qchoice2, value=val).grid(row = loc + 7, column = 7, sticky = W)


#18번 질문
rl1 = [("쉽게 따라 해주는", 3, 1),("의욕적인", 1, 2),("철저한", 4, 3),("활기찬", 2, 4)]
rl2 = [("쉽게 따라 해주는", 3, 1),("의욕적인", 5, 2),("철저한", 4, 3),("활기찬", 2, 4)]
Label(window, text = "18.").grid(row = 12, column = 6)

Label(window, text = "최고").grid(row = 13, column = 6, sticky = W, padx = 5)

for txt, val, loc in rl1:
    Radiobutton(window,text=txt, variable=rchoice1, value=val).grid(row = loc + 13, column = 6, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 7, sticky = W)

for txt, val, loc in rl2:
    Radiobutton(window, variable=rchoice2, value=val).grid(row = loc + 13, column = 7, sticky = W)



#19번 질문
sl1 = [("적극적인", 1, 1),("외향적인", 2, 2),("친근한", 3, 3),("갈등을 피하는", 5, 4)]
sl2 = [("적극적인", 1, 1),("외향적인", 2, 2),("친근한", 3, 3),("갈등을 피하는", 4, 4)]
Label(window, text = "19.").grid(row = 18, column = 6)

Label(window, text = "최고").grid(row = 19, column = 6, sticky = W, padx = 5)

for txt, val, loc in sl1:
    Radiobutton(window,text=txt, variable=schoice1, value=val).grid(row = loc + 19, column = 6, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 19, column = 7, sticky = W)

for txt, val, loc in sl2:
    Radiobutton(window, variable=schoice2, value=val).grid(row = loc + 19, column = 7, sticky = W)


#20번 질문
tl1 = [("자긍심 있는", 2, 1),("공감하는", 3, 2),("공평한", 5, 3),("단호한", 1, 4)]
tl2 = [("자긍심 있는", 2, 1),("공감하는", 3, 2),("공평한", 4, 3),("단호한", 1, 4)]
Label(window, text = "20.").grid(row = 24, column = 6)

Label(window, text = "최고").grid(row = 25, column = 6, sticky = W, padx = 5)

for txt, val, loc in tl1:
    Radiobutton(window,text=txt, variable=tchoice1, value=val).grid(row = loc + 25, column = 6, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 25, column = 7, sticky = W)

for txt, val, loc in tl2:
    Radiobutton(window, variable=tchoice2, value=val).grid(row = loc + 25, column = 7, sticky = W)



#21번 질문
ul = [("절제력 있는", 4, 1),("관대한", 3, 2),("생동감 있는", 2, 3),("주관이 뚜렷한", 1, 4)]
Label(window, text = "21.").grid(row = 0, column = 8)

Label(window, text = "최고").grid(row = 1, column = 8, sticky = W, padx = 5)

for txt, val, loc in ul:
    Radiobutton(window,text=txt, variable=uchoice1, value=val).grid(row = loc + 1, column = 8, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 9, sticky = W)

for txt, val, loc in ul:
    Radiobutton(window, variable=uchoice2, value=val).grid(row = loc + 1, column = 9, sticky = W)


#22번 질문
vl = [("즉흥적인", 2, 1),("내향적인", 4, 2),("강인한", 1, 3),("느긋한", 3, 4)]
Label(window, text = "22.").grid(row = 6, column = 8)

Label(window, text = "최고").grid(row = 7, column = 8, sticky = W, padx = 5)

for txt, val, loc in vl:
    Radiobutton(window,text=txt, variable=vchoice1, value=val).grid(row = loc + 7, column = 8, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 9, sticky = W)

for txt, val, loc in vl:
    Radiobutton(window, variable=vchoice2, value=val).grid(row = loc + 7, column = 9, sticky = W)


#23번 질문
wl = [("남들과 잘 어울리는", 2, 1),("점잖은", 4, 2),("활력 있는", 1, 3),("너그러운", 3, 4)]
Label(window, text = "23.").grid(row = 12, column = 8)

Label(window, text = "최고").grid(row = 13, column = 8, sticky = W, padx = 5)

for txt, val, loc in wl:
    Radiobutton(window,text=txt, variable=wchoice1, value=val).grid(row = loc + 13, column = 8, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 9, sticky = W)

for txt, val, loc in wl:
    Radiobutton(window, variable=wchoice2, value=val).grid(row = loc + 13, column = 9, sticky = W)

#24번 질문
xl = [("매력이 넘치는", 2, 1),("일처리 방식에 만족해 하는", 3, 2),("타인에게 요구가 많은", 1, 3),("기준을 중시하는", 4, 4)]
Label(window, text = "24.").grid(row = 18, column = 8)

Label(window, text = "최고").grid(row = 19, column = 8, sticky = W, padx = 5)

for txt, val, loc in xl:
    Radiobutton(window,text=txt, variable=xchoice1, value=val).grid(row = loc + 19, column = 8, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 19, column = 9, sticky = W)

for txt, val, loc in xl:
    Radiobutton(window, variable=xchoice2, value=val).grid(row = loc + 19, column = 9, sticky = W)


#25번 질문
yl = [("자기 주장을 하는", 1, 1),("체계적인", 4, 2),("협력적인", 3, 3),("경쾌한", 2, 4)]
Label(window, text = "25.").grid(row = 24, column = 8)

Label(window, text = "최고").grid(row = 25, column = 8, sticky = W, padx = 5)

for txt, val, loc in yl:
    Radiobutton(window,text=txt, variable=ychoice1, value=val).grid(row = loc + 25, column = 8, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 25, column = 9, sticky = W)

for txt, val, loc in yl:
    Radiobutton(window, variable=ychoice2, value=val).grid(row = loc + 25, column = 9, sticky = W)

#26번 질문
zl = [("유쾌한", 2, 1),("정교한", 4, 2),("직선적인", 1, 3),("침착한", 3, 4)]
Label(window, text = "26.").grid(row = 0, column = 10)

Label(window, text = "최고").grid(row = 1, column = 10, sticky = W, padx = 5)

for txt, val, loc in zl:
    Radiobutton(window,text=txt, variable=zchoice1, value=val).grid(row = loc + 1, column = 10, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 1, column = 11, sticky = W)

for txt, val, loc in zl:
    Radiobutton(window, variable=zchoice2, value=val).grid(row = loc + 1, column = 11, sticky = W)


#27번 질문
Al = [("변화를 추구하는", 1, 1),("정다운", 3, 2),("호소력 있는", 2, 3),("꼼꼼한", 4, 4)]
Label(window, text = "27.").grid(row = 6, column = 10)

Label(window, text = "최고").grid(row = 7, column = 10, sticky = W, padx = 5)

for txt, val, loc in Al:
    Radiobutton(window,text=txt, variable=Achoice1, value=val).grid(row = loc + 7, column = 10, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 7, column = 11, sticky = W)

for txt, val, loc in Al:
    Radiobutton(window, variable=Achoice2, value=val).grid(row = loc + 7, column = 11, sticky = W)


#28번 질문
Bl = [("정중한", 4, 1),("새로운 것을 시작하는", 1, 2),("낙천적인", 2, 3),("도움을 주려 하는", 3, 4)]
Label(window, text = "28.").grid(row = 12, column = 10)

Label(window, text = "최고").grid(row = 13, column = 10, sticky = W, padx = 5)

for txt, val, loc in Bl:
    Radiobutton(window,text=txt, variable=Bchoice1, value=val).grid(row = loc + 13, column = 10, sticky = W, padx = 15)

Label(window, text = "최저").grid(row = 13, column = 11, sticky = W)

for txt, val, loc in Bl:
    Radiobutton(window, variable=Bchoice2, value=val).grid(row = loc + 13, column = 11, sticky = W)


#결과 버튼
Button(window, text = "완료", command = resultcheck).grid(row = 18, column = 11)

#종료 버튼
Button(window, text = "종료", command = exitfn).grid(row = 29, column = 11)


window.mainloop()
