 
# --- The alysha class ----
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
# ---- my classes
from GUI_Funcs import GUI_Funcs
from eSpeak import eSpeak
eS = eSpeak("alysha")
from filesClass import filesClass
filename = "/home/pi/espeak-data/ai/ai_list"
fc = filesClass(filename)



class alysha:

    # ------------------ Nothing Instantiated -------------------------
    def __init__(self):
        pass 
            
    # ------------------ Open win_alysha  Main Method -----------------
    def open_win_alysha(self):    
        
        # ------------------ Define win_alysha --------------
        win_alysha = Toplevel()
        title = ("Alysha")
        GUI_2 = GUI_Funcs(win_alysha, title)
        GUI_2.WinCenterOffset(400,430,-115,0)
        win_alysha.resizable(False,False)

        # ------------------ Create button Frame ------------
        frm_1_Buttons = Frame(win_alysha)
        frm_1_Buttons.grid(row=1, column=0)        
    
        # ------------------ Add alysha's picture -----------
        global alysha_pic
        alysha_pic = ImageTk.PhotoImage(Image.open("/home/pi/espeak-data/ai/Alysha.jpg"))
        # Add label to hold the picture
        pic_1_alysha = Label(win_alysha, image=alysha_pic)
        pic_1_alysha.grid(row=0, column=0) 

        # ------------------ BUTTON METHODS -----------

        def close_dict():
                get_dict(1)

        # ------------------ Get Dictionary -------------------------------
        def get_dict(flag_dict_open): 

            # ------------ Open the Dictionary ------------
            if flag_dict_open == 0:
                speech = "I will get you the dictionary"
                eS.say(speech)
                
                # ------------ Create a Toplevel() self.win_dictionary -------------- 
                self.win_dict = Toplevel()
                title = "AI Dictionary List"
                GUI_1 = GUI_Funcs(self.win_dict, title)
                GUI_1.WinCoords(635,535,0,0)
                default_bg = self.win_dict.cget("background")
                self.win_dict.resizable(False,False)


                # ------------ Set up Tkinter frames --------
                frm_1_buttons = Frame(self.win_dict)
                frm_1_buttons.grid(row=2, column=0)

                frm_2_txtBox = Frame(self.win_dict)
                frm_2_txtBox.grid(row=1, column=0)

                frm_3_headings = Frame(self.win_dict)
                frm_3_headings.grid(row=0, column=0)

                def no_tab(event):
                    return 'break'


                # ------------ Add the Text Box -------------------
                # ------------ Fonts  FreeMono, Liberation Mono, Noto Sans Mono
                txtBox_1_dict = Text(frm_2_txtBox, height=25, width=60, padx=10, font=("Liberation Mono", 12))
                txtBox_1_dict.grid(row=1, column=0)
                txtBox_1_dict.config(state=NORMAL)
                txtBox_1_dict.bind('<Tab>', no_tab) # <----- DISABLE use of TAB key --------
                # ------------ lines_returned needs to be defined here for methods that follow ------ 
                lines_returned = [] # define the list for the following method

                # ------------  Add Labels to frm_3_headings -------
                lbl_1_num = Label(frm_3_headings, text="#", width=4, relief=RAISED, fg="blue", bg="white")
                lbl_1_num.grid(row=0, column=0, sticky=W)

                lbl_2_word = Label(frm_3_headings, text="Words", width=21, relief=RAISED, fg="blue", bg="lightblue")
                lbl_2_word.grid(row=0, column=1, sticky=W)

                lbl_3_phoneme = Label(frm_3_headings, text="Phonemes", width=21, relief=RAISED, fg="blue", bg="lightblue")
                lbl_3_phoneme.grid(row=0, column=3, sticky=W)

                lbl_5_Rules = Label(frm_3_headings, text="Rules", width=21, relief=RAISED, fg="blue", bg="lightblue")
                lbl_5_Rules.grid(row=0, column=4, sticky=W)


                # ------------  Button Methods -----------------------

                def lock_dict():
                    txtBox_1_dict.config(state=DISABLED)
                    txtBox_1_dict.config(bg="pink")
                    btn_2_lock.config(bg="pink", text="Locked")

                def unlock_dict():
                    txtBox_1_dict.config(state=NORMAL)
                    txtBox_1_dict.config(bg="white")
                    btn_2_lock.config(bg=default_bg, text="Lock")
                    
                def save_dict():
                    speech = "I have saved the dictionary"
                    eS.say(speech)                    
                    lines_returned = read_dict()
                    fc.writeFile(lines_returned)



                # ------------  Add Buttons to frm_1_buttons -----
                lbl_1_no_tabs = Label(frm_1_buttons, text="Tab Key Disabled")
                lbl_1_no_tabs.grid(row=0,column=0)
                
                btn_1_exit = Button(frm_1_buttons, text="Exit", command=close_dict, width=10)
                btn_1_exit.grid(row=0, column=4)

                btn_2_lock = Button(frm_1_buttons, text="Lock", command=lock_dict, width=10)
                btn_2_lock.grid(row=0, column=2)

                btn_3_unlock = Button(frm_1_buttons, text="Unlock", command=unlock_dict, width=10)
                btn_3_unlock.grid(row=0, column=1)

                btn_4_save = Button(frm_1_buttons, text="Save File", command=save_dict, width=10)
                btn_4_save.grid(row=0, column=3)

                # ------------ Get the dictionary file contents ------------------
                lines = fc.readFile() # <--- True = print with line numbers.
                # ------------ Transfer the Lines to the Text Box -------------
                # ------------ Also adding line numbers here ------------------ 
                # ------------ Need to modify this for line numbers > 9999 ------
                for n in range(len(lines)):
                    index = n + 1.0
                    if n+1 < 10:
                        # String single-digit line numbers before line entries.
                        txtBox_1_dict.insert(index,str(n+1) + "    " +lines[n])                        
                    elif n+1 < 100:
                        # String double-digit line numbers before line entries.
                        txtBox_1_dict.insert(index,str(n+1) + "   " +lines[n])                         
                    elif n+1 < 1000:
                        # String triple-digit line numbers before line entries. 
                        txtBox_1_dict.insert(index,str(n+1) + "  " +lines[n])              
                    else: 
                        # String four-digit line numbers before line entries. 
                        txtBox_1_dict.insert(index,str(n+1) + " " +lines[n])


                # ------------ Read the lines back into a list from Text Box --- 

                def read_dict():
                    # ------------ Read the lines back into a list from Text Box ---   
                    lines_returned.clear()
                    # ------------ Get the number of lines in the Text Box ---------
                    line_cnt = int(txtBox_1_dict.index('end-1c').split('.')[0]) 
                    # ------------ Append the lines to Lines_returned list ---------
                    for n in range (1,line_cnt):
                        # --- Convert n to float for indexing the .get() function
                        f = n + 0.0
                        # ------------ Get Lines from the Text box
                        lines_returned.append(txtBox_1_dict.get(f+0.5, f+0.99) + "\n")
                        # ------------ NOTES:
                        # ------------ .get(row.column start, row.column end)
                        # ------------ where row.column is a float.
                        # ------------ f+0.5 moves past the line numbers to start grabing text
                        # ------------ f+0.99 grabs all characters on a line up to column 61
                        # ------------ f is a float equal to integer n (i.e. the current row number)
                    return lines_returned

                read_dict()
                lock_dict()                
                
            # ------------ Close the Dictionary -------------------
            else:
                btn_2_get_dict["state"]=NORMAL
                speech = "I will close the Dictionary"
                eS.say(speech)                 
                self.win_dict.destroy()        
        
        def close_alysha():
                speech = "Goodbye"
                eS.say(speech)   
                win_alysha.destroy()          

        def compile_dict():
            speech = "I have compiled the Dictionary"
            eS.say(speech)
            eS.compile()



        # ------------------ Add buttons to win_alysha  ------------------------------
        btn_2_get_dict = Button(frm_1_Buttons, text="Get Dictionary", command=lambda: get_dict(0))
        btn_2_get_dict.grid(row=0,column=0)

        btn_3_compile_dict = Button(frm_1_Buttons, text="Compile Dictionary", command=compile_dict)
        btn_3_compile_dict.grid(row=0,column=1)

        btn_1_exit_Win_alysha = Button(frm_1_Buttons, text="Close Alysha", command=close_alysha)
        btn_1_exit_Win_alysha.grid(row=0, column=2)



