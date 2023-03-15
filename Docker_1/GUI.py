#import the required packages
import requests
import json

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#import everything from patient and api module
from patient import *
from api import *
from testing import *

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import tkinter as tk
from tkinter import *
from functools import partial 

root = tk.Tk()

def call_result(label_result, n1):  
    num1 = (n1.get())      
    print(num1)
    return num1

def sel():
   if(var.get() == 1):
       url_inp = "http://127.0.0.1:1234/patient"
       k = getReq(url_inp)
       text = Text(root)
       text.insert(INSERT, k)
       text.pack()
       
   elif(var.get() == 2):
       
       def store_input():
          global entry1, entry2, entry3
          entry1 = Name.get()
          entry2 = Age.get()
          entry3 = Diagnosis.get()
          root.destroy()
       msg = "Enter the patient details to be added "
       label.config(text = msg)
          
       root.geometry("450x300")
       user_name = Label(root,
                  text = "Name").place(x = 100,
                                           y = 145)   
       Name = tk.Entry(root,text="Name")
       Name.pack(anchor = CENTER)

       user_age = Label(root,
                  text = "Age").place(x = 100,
                                           y = 165)
       Age = tk.Entry(root)
       Age.pack(anchor = CENTER)

       
       user_diagnosis = Label(root,
                  text = "Diagnosis").place(x = 100,
                                           y = 185)
       Diagnosis = tk.Entry(root)
       Diagnosis.pack(anchor = CENTER)


       B = Button(root, text = "OK", command = store_input)
       B.pack(anchor = S)
       root.mainloop()
       

       url_inp = "http://127.0.0.1:1234/patient/post"
       data_inp = { "name" : entry1, "age" : int(entry2), "diagnosis" : entry3}
       print(postReq(url_inp, data_inp))

       
                

       
   elif(var.get() == 3):
       def store_input():
          global entry1, entry2, entry3, entry4
          entry1 = Name.get()
          entry2 = Age.get()
          entry3 = Diagnosis.get()
          entry4 = ID.get()
          root.destroy()

       msg = "Enter the patient details to be Updated "
       label.config(text = msg)
       
       root.geometry("450x300")
       user_name = Label(root,
                  text = "Name").place(x = 100,
                                           y = 145)   
       Name = tk.Entry(root,text="Name")
       Name.pack(anchor = CENTER)

       user_age = Label(root,
                  text = "Age").place(x = 100,
                                           y = 165)
       Age = tk.Entry(root)
       Age.pack(anchor = CENTER)

       
       user_diagnosis = Label(root,
                  text = "Diagnosis").place(x = 100,
                                           y = 185)
       Diagnosis = tk.Entry(root)
       Diagnosis.pack(anchor = CENTER)

       user_ID = Label(root,
                  text = "ID").place(x = 100,
                                           y = 200)
       ID = tk.Entry(root)
       ID.pack(anchor = CENTER)


       B = Button(root, text = "OK", command = store_input)
       B.pack(anchor = S)
       root.mainloop()
       

       url_inp = "http://127.0.0.1:1234/patient/update/"+ str(entry4)
       data_inp = { "name" : entry1, "age" : int(entry2), "diagnosis" : entry3}
       print(putReq(url_inp, data_inp))

       
   elif(var.get() == 4):
       def store_input():
          global entry1
          entry1 = ID.get()
          root.destroy()

       msg = "Enter the patient ID to be Deleted "
       label.config(text = msg)
       
       ID = tk.Entry(root)
       ID.pack(anchor = CENTER)
       B = Button(root, text = "OK", command = store_input)
       B.pack(anchor = S)
       root.mainloop()
       url_inp = "http://127.0.0.1:1234/patient/delete/"+ entry1
       print(delReq(url_inp))
       
   else:
       root.destroy()
        



var = IntVar()
R1 = Radiobutton(root, text="Fetch all the Patient", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Create new Patient", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Update Existing Patient", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="delete Existing Patient", variable=var, value=4,
                  command=sel)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="Exit", variable=var, value=5,
                  command=sel)
R5.pack( anchor = W)



label = Label(root)
label.pack()
root.mainloop()

