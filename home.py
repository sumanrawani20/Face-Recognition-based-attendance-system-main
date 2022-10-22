from tkinter import *
import tkinter.messagebox
import about1
import contact1

def Home():
    global root
    root.destroy()
    main_display()
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()

def Attandance():
    global root
    root.destroy()
    import check
def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Face Recognition Based Attendance System")
    root.geometry("700x500")
    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Home).pack()
    Label(root,text="").pack()
    Button(root,text='About', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()
    Label(root,text="").pack()
    Button(root,text='Take Attandance', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Attandance).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    Label(root,text="").pack()
    root.mainloop()

main_display()
