from tkinter import *

root = Tk()
root.geometry("600x400")

list_name = ["Mickey Mouse", "Minnie Mouse", "Pikachu", "Donald duck"]
dict_student = { "name" : "Dilean",
                "age" : "10"}
try: 
    print(list_name[6])
    print(dict_student[dad])
    
 exept IndexError :
      messagebox.showinfo("Error", "This index does not exist!")
 exept KeyError : 
      messagebox.showinfo("Error", "This key does not exist!")
      
root.mainloop()
