'''
*위젯: 단순, 컨테이너:다른 위젝을 내부에 넣을 수 있는 것
단순: Button, Canvas, Checkbutton, Entry, Label, Message(label과 비슷 텍스트 축소 자동)등
*컨테이너 위젯: 다른 컴포넌트를 안에 포함 할 수 있는 컴포넌트로서 Frame, Toplevel, LabelFrame, PanedWindow 등

*from tkinter import*
window=Tk() : 제일 먼저 최상위 윈도우를 생성해야 함
var=IntVar() : 생성자로 버튼과 연결해서 사용할 변수 생성(위젯과 연결된 변수)
button=Button(window, text="",commend=클릭시 이벤트 처리할 함수 지정, variable=var(상태를 저장할 변수명), fg/bg="색지정")버튼 생성, (최상위 윈도우, 버튼에 표시 문자, 이벤트 발생할 함수, 상태저장변수, 색지정)
button.pack() : 버튼 글자크기 만큼 화면에 표시
window.mainloop() : 윈도우에서 발생하는 여러가지 이벤트를 처리하는 함수(마우스, 키, 윈도우 시스템에서 발생하는 이벤트 처리)

-배치 관리자 : 위젯의 크기, 위치를 자동 관리
압축 배치 관리자 : pack
격자 배치 관리자 : grid
절대 배치 관리자 : place(x=X좌표, y=Y좌표, width=폭, height=높이)

-위젯.pack(side=TOP/BOTTOM/LEFT/RIGHT,fill=X,padx/pady(위젯간 여백)=픽셀값, ipadx/ipady=픽셀값(내부여백))

-위젯.configure(옵션=값):해당 위젯의 옵션 값을 변경시켜주는 함수

-anchor : 위젯의 위치(N,NE,E,SE,S,SW,W,NW,CENTER(기본값))
'''
from tkinter import *

window=Tk()
'''
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width=FALSE,height=FALSE)
'''
label1=Label(window, text="COOKBOOK~~Python을")
label2=Label(window, text="열심히",font=("궁서체",30),fg="blue")
label3=Label(window, text="공부 중입니다.",bg="magenta",width=20,height=5,anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()