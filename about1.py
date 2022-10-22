from tkinter import *
import tkinter.messagebox
import contact1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    main_display()
def Contact():
    global root
    root.destroy()
    contact1.main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Attendance System")
    root.geometry("700x500")
    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Home).pack()
    Label(root,text="").pack()
    """Button(root,text='About', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()
    Label(root,text="").pack()"""
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    Message(root,text="Bengal College of Engineering (formerly known as BCET) was established by the SKS Educational and Social Trust in 2009. Now it is co-educational college offering courses in the domain of Computing, Electronics and Electrical Engineering. Situated in the posh locality of Durgapur, the Steel City of Bengal the college has robust infrastructure with modern architectonic features. Starting its journey eight years back, the institute has already positioned itself among the premier engineering institutes in the Asansol-Durgapur industrial belt.").pack()
    root.mainloop()
