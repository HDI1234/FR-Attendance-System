from tkinter import *
from Functions import *
from attendanceImage import *
from tkinter import filedialog
import tkinter.messagebox
from PIL import ImageTk, Image, ImageGrab
import pyautogui, time

def callStartImage():

    tkinter.messagebox.showinfo("Info", "Please open your video conferencing app to begin recording attendance.")
    for i in range(3):
        ss = pyautogui.screenshot()
        ss.save(f"class/SS{i}.jpg")
        time.sleep(5)
    startImage("class")
    tkinter.messagebox.showinfo("Info", "Attendance Record has been completed. Thank you.")

root = Tk()
root.title('Facial Recognition Attendance Program for Online Classes')
root.minsize(910, 750)
root.maxsize(910, 750)
root.configure(background="#ffffff")

heading = Label(root, text="Automated Attendance System", fg="#80182A")
heading.configure(font=("Cambria", 35))
heading.pack(fill="x")

img = ImageTk.PhotoImage(Image.open('Logo/runtime_ninjas.png'))
labelImage = Label(root, image=img, borderwidth=0)
labelImage.pack(pady=20)

btn2 = Button(root, text="Start Attendance", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=callStartImage).pack(pady=(0, 20))
btn4 = Button(root, text="Open Attendance Sheet", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=openExcelImage).pack(pady=(0, 20))
btn5 = Button(root, text="e-Attendance", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=openReadme).pack(pady=(0, 20))

root.mainloop()