# Substitution encryption technique.
from tkinter import *
from tkinter import messagebox
import webbrowser
import caesar_cipher_GUI as ccg
import hill_ciphers_GUI as hcg
import monoalphabetic_GUI as mg
import one_time_pad_GUI as otpg
import playfare_GUI as pg
import polyalphabetic_GUI as polg

font1 = ("Bookman Old Style Light", 19, "italic")
font2 = ("Cascadia Code Regular", 16)
font3 = ("Corbel Light", 12, "bold", "italic")
font4 = ("Pristina", 12)
class Main_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Substitution encryption and decryption algos.👩‍💻👩‍💻👩‍💻👩‍💻")
        self.root.geometry("600x700")
        # initial labels
        lbltitle = Label(self.root, bd=12, relief=RIDGE, text="Substitution encryption and decryption", fg="red",
                         bg="white", font=font1)
        lbltitle.pack(side=TOP, fill=X)
        head = Label(self.root, text="Algorithms.👇👇", bg="white", font=font2)
        head.pack()
        # all buttons
        cis = Button(self.root, command=self.caeser_call, text="Caesar Cipher", bg="green", fg="white",
                                 font=font3, width=15, pady=2)
        cis.pack(pady=16)
        mo = Button(self.root, command=self.monoalphabetic_call, text="Monoalphabetic Cipher", bg="green", fg="white",
                     font=font3, width=18, pady=2)
        mo.pack(pady=16)
        pl = Button(self.root, command=self.playfair_Cipher_call, text="Playfair Cipher", bg="green", fg="white",
                     font=font3, width=15, pady=2)
        pl.pack(pady=16)
        hi = Button(self.root, command=self.hill_Cipher_call, text="Hill Cipher", bg="green", fg="white",
                     font=font3, width=15, pady=2)
        hi.pack(pady=16)
        po = Button(self.root, command=self.Polyalphabetic_Cipher, text="Polyalphabetic Cipher", bg="green", fg="white",
                     font=font3, width=18, pady=2)
        po.pack(pady=16)
        ot = Button(self.root, command=self.One_Time_Pad_call, text="One-Time Pad", bg="green", fg="white",
                    font=font3, width=15, pady=2)
        ot.pack(pady=16)
        exittitle = Label(self.root, bd=12, relief=GROOVE, text="Hey! Do you wanna exit from this mess?☹️", fg="red",
                         bg="white", font=font1)
        exittitle.pack(fill=X)
        button1 = Button(self.root, text='Exit Application', command=self.exit_application, bg='brown', fg='white',
                         font=font3)
        button1.pack(pady=16)
        # footer
        bottomframe = Frame(self.root, bg="#fcd50f", width=80)
        bottomframe.pack(side=BOTTOM, fill=X)
        text = Label(bottomframe, text="-by Anon Anderson(Portfolio)", font=font4, cursor="hand2")
        text.pack(side=LEFT, padx=16, pady=16)
        text.bind("<Button-1>", lambda e:
        self.callback("https://64a851a51f46e6124e49253c--stunning-bombolone-f05aa8.netlify.app/"))
        link = Label(bottomframe, text="Open full directory in GitHub", font=font4, fg="#b54c05", cursor="hand2")
        link.pack(side=RIGHT, padx=16, pady=16)
        link.bind("<Button-1>", lambda e:
        self.callback("https://github.com/ArnabAdhikar"))
    def caeser_call(self):
        ccg.build()
    def monoalphabetic_call(self):
        mg.build()
    def playfair_Cipher_call(self):
        pg.build()
    def hill_Cipher_call(self):
        hcg.build()
    def One_Time_Pad_call(self):
        otpg.build()
    def Polyalphabetic_Cipher(self):
        polg.build()
    def exit_application(self):
        msg_box = messagebox.askquestion('Exit Application?', 'Broo... You are so rude😔', icon='warning')
        if msg_box == 'yes':
            root.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    def callback(self, url):
        webbrowser.open_new_tab(url)
if __name__ == "__main__":
    root = Tk()
    m = Main_GUI
    ob = m(root)
    root.mainloop()
