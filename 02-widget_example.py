#import tkinter
from tkinter import * #her şeyini import eder

my_window = Tk()
my_window.title("tkinter python")
my_window.minsize(width = 600, height= 600)
my_window.config(padx=20, pady=20)

#sağ tık refactor - rename tüm labelların ismini değiştirir mesela my_label
my_label = Label(text ="my label")
my_label.config(bg ="black")
my_label.config(fg ="white")
my_label.config(padx=10, pady=10)
my_label.pack()

def button_clicked():
    print("button clicked")
    print(my_entry.get())
    print(my_text.get("1.0",END)) # index ister
    # 1 hangi satırdan başladığı 0 hangi karakterden başladığı

my_button = Button(text ="button", command = button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

my_entry = Entry(width=20) #kısa
my_entry.focus()
my_entry.pack()

#multiline
my_text = Text(width=30,height = 10) #uzun
my_text.focus() #odaklan
my_text.pack()

#scale
def scale_selected(value):
    print(value)
my_scale = Scale(from_=0, to=50,command = scale_selected)
my_scale.pack()

def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_= 0, to=50, command =spinbox_selected)
my_spinbox.pack()

def checkbutton_selected():
    print(check_state.get())

check_state = IntVar() #checkbutton seçildi mi seçilmedi mi
my_checkbutton = Checkbutton(text= "check", variable= check_state, command= checkbutton_selected )
my_checkbutton.pack()

#radio button

def radio_selected():
    print(radio_checked_state.get())
radio_checked_state =IntVar()
my_radio_button1 = Radiobutton(text= "1.option", value= 10, variable= radio_checked_state, command= radio_selected)
my_radio_button2 = Radiobutton(text= "2.option", value= 20, variable= radio_checked_state, command= radio_selected)
my_radio_button1.pack()
my_radio_button2.pack()

#listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection())) #güncel seçileni gösterir

my_listbox = Listbox()
name_list = ["ümran", "meryem", "karabakal"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<listbox_selected>>',listbox_selected) #bağlama

my_listbox.pack()

my_window.mainloop()