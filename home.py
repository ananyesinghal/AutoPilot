import mysql.connector as sq
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image

root = tk.Tk()
root.geometry('1000x1000')
root.title("Welcome to AutoPilot System")

idvar = tk.StringVar(root)
passvar = tk.StringVar(root)

label_1 = Label(root, text="Login with your credentials to access the system.", width=50, font=("bold", 25))
label_1.place(x=10, y=40)

label_2 = Label(root, text="Enter Registration Number : ",width=20,font=("bold", 10))
label_2.place(x=200,y=650)

entry_2 = Entry(root, textvariable=idvar)
entry_2.place(x=700,y=650)

label_3 = Label(root, text="Enter Password : ",width=20,font=("bold", 10))
label_3.place(x=200,y=700)

entry_3 = Entry(root, textvariable=passvar)
entry_3.place(x=700,y=700)

canvas = Canvas(root, width = 500, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("./img/homeimg.jpg"))  
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.place(x=250, y=80)

mydb = sq.connect(
  host="localhost",
  user="root",
  password="Anne2912.as@mysql;",
  database="autopilot"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS credentials (regno VARCHAR(255), password VARCHAR(255))")

mycursor.close()
mydb.close()

print(mydb)

root.mainloop()