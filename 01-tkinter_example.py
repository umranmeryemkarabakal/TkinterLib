import tkinter

def click_button(): #click button yazmadan önce tanımlamalıyız
    print("button clicked")
    #genel olarak sıra sorun değildir command harici
    my_entry.get() #ne yazıldıysa direk string olarak alabiliriz

window = tkinter.Tk()
window.title("python tkinter")
window.minsize(width=450,height=300)

my_label = tkinter.Label(text="this is a label", font =('monospace',16,"normal"))
my_label.config(bg = "black", fg = "white")
#my_label.pack(side = "top") #side = right sağa hizzalar, top üste, bottom aşağıya
#my_label.place(x =0,y=0) #nereye koymak istedini sorar
my_label.grid(row=0, column=0) #sıralar row, kolonlar column


my_button = tkinter.Button(text="this is a button",command = click_button)
#my_button.pack()
my_button.place(x = 225-44.5, y = 150-13)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
my_button.grid(row = 1, column =1)

my_entry = tkinter.Entry(width=20)
#my_entry.pack(side = "top")
#my_entry.place(x=450-150,y=300-40)
my_entry.grid(row=3 , column=2)

window.mainloop()