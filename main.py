from tkinter import *
import pyshorteners
root = Tk()
root.title("Url shortener")

root.geometry("500x500")

def shorten():
    if out_input.get():
        out_input.delete(0, END)
    if my_input.get():
        url = pyshorteners.Shortener().tinyurl.short(my_input.get())
        out_input.insert(END, url)
my_label = Label(root, text="Enter your link", font=("Times", "24", "bold italic"))
my_label.pack()

my_input = Entry(root, font=("Times", "24", "bold italic"), width=30)
my_input.pack(pady=20)

my_button = Button(root, font=("Times", "24", "bold italic"), text="Shorten", command=shorten)
my_button.pack(pady=20)

s_label = Label(root, text="shortened link",font=("Times", "14", "bold italic"))
s_label.pack(pady=40)

out_input = Entry(root, font=("Times", "24", "bold italic"), width=30, bd=0, bg="systembuttonface", justify=CENTER)
out_input.pack(pady=10)



root.mainloop()