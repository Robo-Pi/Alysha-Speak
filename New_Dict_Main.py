
import subprocess as cmdLine
cmdLine.call("clear")
# --------- Import Tkinter stuff:
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
# --------- Import my GUI Functions
from GUI_Funcs import GUI_Funcs
# --------- Import and Instantiate eSpeak class
from eSpeak import eSpeak
eS = eSpeak("alysha")
# --------- Import and Instantiate alysha class
from New_alysha import alysha
alysha = alysha()
global dict_filename

# --------- MAIN GUI PROGRAM STARTS HERE ------------------
# Define win_main and place it using the GUI_Funcs Class
win_main = Tk()
title = "Alysha Dictionary App"
GUI_1 = GUI_Funcs(win_main, title)
GUI_1.WinCenterOffset(400,150,200,0)
default_bg = win_main.cget("background")

# --------- Create frames to hold wigets in columns -----
frame_1 = Frame(win_main)
frame_1.grid(row=1, column=0)

frame_2 = Frame(win_main)
frame_2.grid(row=1, column=1)

frame_3 = Frame(win_main)
frame_3.grid(row=1, column=2)

# --------- Headers for columns ----------
header_1 = Label(win_main, text='Path = Default', bg="lightblue")
header_1.grid(row=0, column=0, columnspan=3)

# --------- Methods for Menu Bar go here --------------

def get_filename():
    dict_filename = filedialog.askopenfilename\
    (filetypes=(("All files","*"),\
        ("Python Files",".py")))
    header_1.config(text="Path = " + str(dict_filename))

# --------- Create the Menu Bar -----------------
menu_bar = Menu(win_main)
win_main.config(menu=menu_bar)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Get Dictionary File Path", command=get_filename)
# file_menu.add_command(label="Exit", command=win_main.quit)

# --------- Methods for wigets below go here: ----------

# --------- Add widgets to frame_1 -------------
lbl_1_word = Label(frame_1, text='Enter Word', width=12, pady=15)
lbl_1_word.grid(row=0, column=0, columnspan=2, sticky=E)

lbl_2_phonemes = Label(frame_1, text="Phonemes", width=12, pady=5)
lbl_2_phonemes.grid(row=1, column=0, columnspan=2, sticky=E)

lbl_3_save = Label(frame_1, text="Save Word?", width=12, pady=5)
lbl_3_save.grid(row=3, column=0, columnspan=2, sticky=E)

lbl_4_null = Label(frame_1, text="", width=12, pady=5)
lbl_4_null.grid(row=2, column=0, columnspan=2, sticky=E)


# --------- Methods for wigets below go here: ----------

# --------- Add Widgets to frame_2 -------------------
tbx_1_word = Entry(frame_2, width=15, font=("Liberation Mono", 12), relief=SUNKEN, borderwidth=5)
tbx_1_word.grid(row=0, column=0, columnspan=2)
tbx_1_word.insert(0, "word")

tbx_2_phonemes = Entry(frame_2, width=15, font=("Liberation Mono", 12), relief=SUNKEN, borderwidth=5)
tbx_2_phonemes.grid(row=1, column=0, columnspan=2)
tbx_2_phonemes.insert(0, "phonemes")

tbx_null_3 = Label(frame_2, text=" ") # --------- null LABLE ----
tbx_null_3.grid(row=2, column=0, columnspan=2)

btn_4_yes = Button(frame_2, text="Yes", width=2, pady=5)
btn_4_yes.grid(row=3, column=0)

btn_5_no = Button(frame_2, text="No", width=2, pady=5)
btn_5_no.grid(row=3, column=1, sticky=W)

# btn_4_repeat = Button(frame_2, text="Repeat", width=10, pady=5)
# btn_4_repeat.grid(row=2, column=0)

# --------- Methods for Buttons ----------
def new_word():
    pass


# --------- Define a Message Box
def popUp():
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    response = messagebox.askquestion("Question Box", "Do you want to continue?")
    print(response) 


def repeat_word():
    pass

# --------- Add Buttons onto frame_3
btn_1_Openwin_alysha = Button(frame_3, width=10, text="Open Alysha", command=alysha.open_win_alysha)
btn_1_Openwin_alysha.grid(row=0, column=0)

btn_2_msgBox = Button(frame_3, width=10, text="Repeat", command=repeat_word)
btn_2_msgBox.grid(row=2, column=0)

btn_3_new_word = Button(frame_3, width=10, text="New Word", command=new_word)
btn_3_new_word.grid(row=1, column=0)

btn_4_exit = Button(frame_3, width=10, text="Exit", command=win_main.quit)
btn_4_exit.grid(row=3, column=0)

# --------- Bottom of Program -----------
win_main.mainloop()
