from tkinter import *
import tkinter.messagebox

import about1

def Home():
    global root
    root.destroy()
    import home
def About():
    global root
    root.destroy()
    about1.main_display()
def Contact():
    global root
    root.destroy()
    main_display()
def Exit():
    wayOut = tkinter.messagebox.askyesno("Attendance System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("700x500")
    Label(root,text='Face Recognition Based Attendance System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Home', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Home).pack()
    """Label(root,text="").pack()
    Button(root,text='About', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=About).pack()
    Label(root,text="").pack()
    Button(root,text='Contact', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Contact).pack()"""
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit).pack()
    var="""1

Chairman	Shri. S.K. Sharma	
Phone: +91-343-253 3188
2

Vice-Chairman	
Shri Mayank Gautam

Email: vc@sksgi.com
3	Director (Admn) - SKSEST	Prof.(Dr) A C Ganguli	Telefax : +91-343-253 3186 
Email: acg_recd@yahoo.co.in
4

Principal	
Prof (Dr) Sanchita Bandyopadhyay

Mobile: 8900245667 
E-mail: sanchiban1@rediffmail.com
E-mail: principal@bcedgp.ac.in

5

Manager 
(Admin & Public Relation)	
Mr B Basu Thakur

Ph: 8170021128
Mob: 09434332501"""
    Message(root,text=var,width="1500").pack()
    root.mainloop()

