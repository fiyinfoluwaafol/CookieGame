import tkinter as tk
from tkinter import Text


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg='#ffffcc') #this is kinda like the border type thingy. color code is baige
canvas.pack()

frame = tk.Frame(root, bg="White")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #indentationto make the broder centered

Start = tk.Button(frame, text="Start", padx=10,
                  pady=10, fg="white", bg="black")#start button :D
Start.pack()

canvas.create_text(350, 75, text="Cookie Cracker", fill="black", font=('Helvetica 15 bold'))
canvas.pack()
root.mainloop()


#def print_hi(name):
        #Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, tomiwa')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
