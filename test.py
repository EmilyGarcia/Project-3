from tkinter import *
"""
master = Tk()

listbox = Listbox(master, selectmode=SINGLE).grid(row=3, column=2, sticky=W, pady=4)
listbox.grid()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
    
Button(master, text=listbox.get(ACTIVE)).grid(row=3, column=2, sticky=W, pady=4)

mainloop()
"""
from tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print ("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()





