from tkinter import *
from tkinter import ttk
from pygame import mixer
import scenes

root = None
mainmenu_frame = None
mysterymenu_frame = None
images = []
#testing out how editing a forked repo works when u want to push the changes to the msin of the original repo
# Audio init
mixer.init()
mixer.music.load("./audio/Cookie_Crumble.wav")
mixer.music.play(loops=-1)

def init_root():
    global root
    root = Tk(className="Cookie")
    root.geometry("800x600")

def close_mainmenu():
    global mainmenu_frame
    if mainmenu_frame != None:
        mainmenu_frame.destroy()
        mainmenu_frame = None

def create_mysterymenu(tag="0"):
    global mainmenu_frame
    global mysterymenu_frame
    global root
    close_mainmenu()
    close_mysterymenu()

    mysterymenu_frame = ttk.Frame(root)
    mysterymenu_frame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1) 

    for scene in scenes.scenes:
        if scene["tag"] == tag: 
            image_frame = ttk.Frame(mysterymenu_frame)
            image_frame.place(anchor=CENTER, relx = 0.5, rely = 0.15)
            
            # Add images, maximum of 6 currently
            if len(scene["images"]) > 0:
                image0 = PhotoImage(file="./images/" + scene["images"][0] + ".png")
                ttk.Label(image_frame, image=image0).grid(column=0, row=0)
 
            if len(scene["images"]) > 1:
                image1 = PhotoImage(file="./images/" + scene["images"][1] + ".png")
                ttk.Label(image_frame, image=image1).grid(column=1, row=0)

            if len(scene["images"]) > 2:
                image2 = PhotoImage(file="./images/" + scene["images"][2] + ".png")
                ttk.Label(image_frame, image=image2).grid(column=2, row=0)

            if len(scene["images"]) > 3:
                image3 = PhotoImage(file="./images/" + scene["images"][3] + ".png")
                ttk.Label(image_frame, image=image3).grid(column=3, row=0)

            if len(scene["images"]) > 4:
                image4 = PhotoImage(file="./images/" + scene["images"][4] + ".png")
                ttk.Label(image_frame, image=image4).grid(column=4, row=0)

            if len(scene["images"]) > 5:
                image5 = PhotoImage(file="./images/" + scene["images"][5] + ".png")
                ttk.Label(image_frame, image=image5).grid(column=5, row=0)
            
            desc_lbl = ttk.Label(mysterymenu_frame, text=scene["description"], wraplength=500)
            desc_lbl.place(anchor=CENTER, relx=0.5, rely=0.45)

            a_btn = ttk.Button(mysterymenu_frame, text=scene["a"], command=lambda _tag = scene["a_next"]: create_mysterymenu(_tag))
            a_btn.place(anchor=CENTER, relx=0.5, rely="0.7")
            
            b_btn = ttk.Button(mysterymenu_frame, text=scene["b"], command=lambda _tag = scene["b_next"]: create_mysterymenu(_tag))
            b_btn.place(anchor=CENTER, relx=0.5, rely="0.75")
            
            c_btn = ttk.Button(mysterymenu_frame, text=scene["c"], command=lambda _tag = scene["c_next"]: create_mysterymenu(_tag))
            c_btn.place(anchor=CENTER, relx=0.5, rely="0.8")
            
            root.mainloop()


def close_mysterymenu():
    global mysterymenu_frame
    if mysterymenu_frame != None:
        mysterymenu_frame.destroy()
        mysterymenu_frame = None

def create_mainmenu():
    global mainmenu_frame
    mainmenu_frame = ttk.Frame(root)
    mainmenu_frame.place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=1, relheight=1);
    
    title_lbl = ttk.Label(mainmenu_frame, text="Family secrets", font=("Arial, 25"))
    title_lbl.place(anchor=CENTER, relx=0.5, rely=0.15);
    
    desc_lbl = ttk.Label(mainmenu_frame, text="This is a mystery game about a detective figuring out who broke into a families house.You make choices, ask questions and solve the mystery! In the game you have to use little context clues to figure our the whole story, your diffrent questions you can ask give you diffrent pieces of information, so you either have to get the perfect combination of questions(the ideal path), or you could make your own path and who knows you might still get the culprit! \n\nAnd lastly have fun! We had fun making this!", wraplength=500,  justify="center") # This is the description text, stating what the game is about and other important information.
    desc_lbl.place(anchor=CENTER, relx=0.5, rely=0.4)
    
    start_btn = ttk.Button(mainmenu_frame, text="Start", command=create_mysterymenu)
    start_btn.place(anchor=CENTER, relx=0.5, rely=0.65)
    exit_btn = ttk.Button(mainmenu_frame, text="Exit", command=root.destroy)
    exit_btn.place(anchor=CENTER, relx=0.5, rely=0.7)
    
    credits_lbl = ttk.Label(mainmenu_frame, text="By Oluwatomiwa Shobowale, Oghenetega Gbejewoh, Kamsi Onubogu and Fiyinfoluwa Afolayan")
    credits_lbl.place(anchor=CENTER, relx=0.5, rely=0.95)

def main():
    init_root()
    create_mainmenu() 
    root.mainloop()

main()
