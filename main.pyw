from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pyautogui
import time
import pydirectinput as pyauto
# while True:
#     if keyboard.is_pressed("a"):
#         print("You pressed 'a'.")
#         break





box_pos = False




root = Tk()
text_pos = StringVar()
text_status = StringVar()
def setPos():
    global box_pos
    box_pos = pyautogui.position()
    print(box_pos)
    text_pos.set(f"cursor: x={box_pos.x} y={box_pos.y}")
    
    root.update()


text_pos.set(f"cursor: โปรดนำเมาส์แล้วเอาไปชี้ที่ ใช้ แล้วกด Ctrl+s")
# root.geometry("175x180")
root.title("โปรแกรมเปิดกล่อง")
root.attributes("-topmost", True)
frm = ttk.Frame(root, padding=10)
frm2 = ttk.Frame(root, padding=10)
frm3 = ttk.Frame(root, padding=10)
frmRuning = ttk.Frame(root, padding=10)
entryNumBox = ttk.Entry(width=6)
def runing(num, pos):
    for i in range(num):
        pyauto.click(pos.x, pos.y)
        pyauto.press("enter")
        time.sleep(4)
        pyauto.press("enter")
        text_status.set(f"เปิดไปแล้ว: {i+1} กล่อง\n เหลือ: {num-(i+1)} กล่อง")
        root.update()
        
    
    text_status.set(f"เปิดครบ: {num} กล่อง")
    root.update()
def startAuto():
    global box_pos
    try:
        num_box = int(entryNumBox.get())
        if(box_pos==False):
            tkinter.messagebox.showerror(title="ยังไม่ได้ตั้งกล่อง", message="โปรดตั้ง cursor ตำแหน่งกล่อง")
        else:
            frm3.grid_forget()
            frmRuning.grid()
            root.update()
            runing(num_box, box_pos)
            frm3.grid()
            root.update()
            
    except:
        tkinter.messagebox.showerror(title="ตัวเลขไม่ถูกต้อง", message="โปรดกรอจำนวนกล่องที่ต้องการเปิดให้ถูกต้อง")
    

frm.grid()
frm2.grid()
frm3.grid()


ttk.Label(frm, text="จำนวนกล่อง:").grid(column=0, row=0)
entryNumBox.grid(column=1, row=0)

ttk.Label(frm2, textvariable=text_pos).grid()
ttk.Label(frmRuning, textvariable=text_status).grid()

ttk.Button(frm3, text="เริ่ม", command=startAuto).grid()

root.bind('<Control-s>', lambda event: setPos())

root.mainloop()
