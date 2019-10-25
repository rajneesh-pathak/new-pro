"""word=input("Enter the information word")
error=input("Enter the error")
code=""

for i in range(len(word)):
	if((word[i]=='1') and (error[i]=='1')):
		code[i].append('0')
	else:
		code[i].append(word[i])

#INFORMATION WORD WITH THE ERROR	
print("The code word is : ", code)

#PARITY BIT CHECK SUM
s1=((int)code[1] + (int)code[2] + (int)code[3] + (int)code[5])%2 
s2=((int)code[2] + (int)code[3] + (int)code[4] + (int)code[6])%2
s3=((int)code[1] + (int)code[2] + (int)code[4] + (int)code[7])%2

#SYNDROME TABLE
if((s1==0) and (s2==1) and (s3==1)):
	e=["0001000"]
elif((s1==1) and (s2==1) and (s3==0)):
	e=["0010000"]
elif((s1==1) and (s2==1) and (s3==1)):
	e=["0100000"]
elif((s1==1) and (s2==0) and (s3==0)):
	e=["1000000"]
else:
	e=["0000"]
	e.append(s1)
	e.append(s2)
	e.append(s3)
	
word=""
#DECODING
for i in range(8):
	if(code[i]=='1' and e[i]=='1'):
		word[i]='0'
		
print("The decoded word is : ", word)
"""

from tkinter import *

col_bg = "white"
col_fg = "grey"

fenster = Tk()
fenster.title("Hello Windowtitle")
fenster.geometry("500x300")
fenster.configure(background="white")


# Definition Text widget
def buildnew_textwidget(col_bg,col_fg):
    T = Text(fenster, height=300, width=200, bg=col_bg, fg=col_fg, bd=0)
    T.pack()
    T.insert(END, "")
buildnew_textwidget(col_bg, col_fg)


# Definition Colors
def Rot():
    col_bg = "red"
    col_fg = "black"
    buildnew_textwidget(col_bg, col_fg)

def Gelb():
    col_bg = "yellow"
    col_fg = "black"
    buildnew_textwidget(col_bg, col_fg)

menu = Menu(fenster)

# Colorsheme
colorsheme = Menu(menu, tearoff=0, background='black',
foreground='#D9CB9E', activebackground='#D9CB9E',
activeforeground='#374140', activeborderwidth=4)

menu.add_cascade(label="Colorsheme", menu=colorsheme)
colorsheme.add_command(label="Rot", command=Rot)
colorsheme.add_command(label="Gelb", command=Gelb)

fenster.config(menu=menu)

mainloop( )