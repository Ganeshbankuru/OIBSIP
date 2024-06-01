# this code for creating random passwords for the users , there is user choice  what type of charecters  they want for their password ,and also have copy 
# button for copying the password to the clipboard and also you can save the passoword with the date in the separate text file.
import tkinter as tk
import random as rd
from datetime import datetime

def button_press(var1,var2,var3,var4,entry_len):
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = [1,2,3,4,5,6,7,8,9,0]
    sym = ['!','@','#','$','%','^','&','*','(',')','_','+','-','`','~','/','.',',','?','<','>']

    list1 = []
    k=int(entry_len.get())
    a=var1.get()
    if a == 1:
        list1+=small
    b=var2.get()
    if b == 1:
        list1+=big
    c=var3.get()
    if c == 1:
        list1+=num
    d=var4.get()
    if d == 1:
        list1+=sym

    if list1:
        choice = rd.choices(list1, k=k)
        entry_psw.delete(0, tk.END)
        entry_psw.insert(tk.END, choice)
    else:
        entry_psw.delete(0, tk.END)
        entry_psw.insert(tk.END, "Please select at least one character set")


def copy_clipboard(entry_psw):
    root.clipboard_append(entry_psw.get())

def save_password(entry_psw):
    password = entry_psw.get()
    if password:
        current_datetime = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        with open("passwords.txt", "a") as f:
            f.write(f"{current_datetime}: {password}\n")
        lbl_clarify = tk.Label(root,text="your password is saved succesfully in passwords.txt file",bg='gray',fg="blue",font=("arial",12))
        lbl_clarify.pack(padx=10,pady=10)

root = tk.Tk()
root.geometry("400x400")
root.title("Random Password Generator")
root.config(background='gray')

lbl_title = tk.Label(root,text="Password Generator",bg='gray',font=("arial",18))
lbl_title.pack(padx=10,pady=10)

main_frame = tk.Frame(root,bg='gray')

lbl_len = tk.Label(main_frame,text="length of password",bg='gray',font=("arial",12))
lbl_len.grid(row=0,column=0,padx=10,pady=10)

entry_len = tk.Entry(main_frame,font=("arial",12))
entry_len.grid(row=0,column=1,padx=10,pady=10)


lbl_include = tk.Label(main_frame,text="Include",font=("arial",12),bg='gray')
lbl_include.grid(row=1,column=0,sticky='ew')

checkbox_frame = tk.Frame(main_frame,bg='gray')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

cb_small = tk.Checkbutton(checkbox_frame,text="(a-z)",bg='gray',font=("arial",10),variable=var1)
cb_small.grid(row=0,column=0,sticky="ew")
cb_big = tk.Checkbutton(checkbox_frame,text="(A-Z)",bg='gray',font=("arial",10),variable=var2)
cb_big.grid(row=0,column=1,sticky="ew")
cb_num = tk.Checkbutton(checkbox_frame,text="(0-9)",bg='gray',font=("arial",10),variable=var3)
cb_num.grid(row=0,column=2,sticky="ew")
cb_sym = tk.Checkbutton(checkbox_frame,text="sym",bg='gray',font=("arial",10),variable=var4)
cb_sym.grid(row=0,column=3,sticky="ew")

checkbox_frame.grid(row=1,column=1,sticky='ew',pady=20)

main_frame.pack(padx=10,pady=10)


bn_generate = tk.Button(root,text="Generate",font=("arial",12),bg='#F2AF33',fg='navyblue')
bn_generate.config(command=lambda: button_press(var1,var2,var3,var4,entry_len))
bn_generate.pack(padx=10,pady=10)

res_frame = tk.Frame(root,bg='gray')

lbl_psw = tk.Label(res_frame,text="Your password",bg='gray',font=("arial",12))
lbl_psw.grid(row=0,column=0,pady=10,padx=10)

entry_psw = tk.Entry(res_frame,font=("arial",12))
entry_psw.grid(row=0,column=1,pady=10,padx=10)

bn_copy = tk.Button(res_frame,text="copy",font=("arial",12),bg='white')
bn_copy.config(command=lambda: copy_clipboard(entry_psw))
bn_copy.grid(row=0,column=2)

res_frame.pack(padx=10,pady=10)

bn_save = tk.Button(root, text="Save", font=("arial", 12), bg='#44F618', fg='#071403')
bn_save.config(command=lambda: save_password(entry_psw))
bn_save.pack(padx=10, pady=10)

root.mainloop()
