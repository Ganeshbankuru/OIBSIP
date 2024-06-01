import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

# function for getting values from entry box and convert them to the respective types
# then claculate the body mass index and gives result as per the value
def button_press(entry_weight,feet_entry,inch_entry):
    try:
        a = float(entry_weight.get())
        b = int(feet_entry.get())*0.3048
        c = int(inch_entry.get())*0.0254
        bmi = round(a/(b+c)**2,2) # rounding floating value to two decimals of bmi
        lbl_bmi.config(text=f"BMI:{bmi}") # printing bmi on gui by configuring the lable
        if bmi<16.5:
            lbl_res.config(text='person is severly underweight',fg="red") #printing result
        elif bmi<18.5:
            lbl_res.config(text='person is underweight',fg="brown")
        elif bmi>18.5 and bmi<24.9:
            lbl_res.config(text='person is Normalweight',fg='green')
        elif bmi>24.9 and bmi<29.9:
            lbl_res.config(text='person is Overweight',fg='tomato')
        elif bmi>=30:
            lbl_res.config(text='person has Obesity',fg='red')
        lbl_error.config(text="")
    except ValueError:
        lbl_error.config(text="You provide insufficient data")


root = tk.Tk() #starting the tkinter module
root.title("Body Mass Index")
root.geometry("400x400")
root.config(bg='gold') #defining background colour

# creating lable for title
lbl_title = tk.Label(root,text='Body Mass Index',font=('bookman',18),bg='gold')
lbl_title.pack(padx=10,pady=10)

#creating frame for putting the lables and entries together
bmi_frame = tk.Frame(root,bg='gold')

#creating lable for entering weight
lbl_weight = tk.Label(bmi_frame,text="Enter Weight (kg)",font=('rockwell',12),bg='gold')
lbl_weight.grid(row=0,column=0,padx=10,pady=10,sticky='ew')

#creating entry for weight
entry_weight = tk.Entry(bmi_frame,width=20)
entry_weight.grid(row=0,column=1,padx=10,pady=10,sticky='ew')

#creating lable for entering height
lbl_height = tk.Label(bmi_frame,text="Enter Height(feet&inch)",font=('rockwell',12),bg='gold')
lbl_height.grid(row=1,column=0,padx=10,pady=10)

#creating frame for putting feet and inch entry side by side
height_frame = tk.Frame(bmi_frame,bg='gold')

feet_entry = tk.Entry(height_frame,width=10) #creating entry for feets
feet_entry.grid(row=0,column=0,padx=10,pady=10,sticky='ew')

inch_entry = tk.Entry(height_frame,width=10) #creating entry for inches
inch_entry.grid(row=0,column=1,padx=10,pady=10,sticky='ew')

height_frame.grid(row=1,column=1,padx=10,pady=10,sticky='ew') #closing height_frame

bmi_frame.pack(padx=10,pady=10) #closing bmi_frame

#creating button for bmi claculation and also create an even while pressing button
bmi_button = tk.Button(root,text="calculate",bg='skyblue',font=("italic",12),bd=5,activebackground='orange')
bmi_button.config(command=lambda:button_press(entry_weight,feet_entry,inch_entry)) #event is calling function button_press
bmi_button.pack(padx=10,pady=10)

#creating a lable for showing the value of bmi
lbl_bmi = tk.Label(root,text=f"BMI:",bg='gold',font=("algerian",12))
lbl_bmi.pack(padx=10,pady=10)

#creating lable for showing the result of the bmi
lbl_res = tk.Label(root,text='Result',font=("rockwell",14),bg="gold")
lbl_res.pack(padx=10,pady=10)

lbl_error = tk.Label(root,font=("rockwell",12),fg='red',bg='gold')
lbl_error.pack(padx=10,pady=10)

root.mainloop()#end loop for continous creation of widgets