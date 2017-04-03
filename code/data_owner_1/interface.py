#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from get_connection import *
from get_key import *
import Tkinter
import tkMessageBox


class mainFrame:
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title('Secure Protocol Systems')
        self.root.geometry('600x300')
        self.root.resizable(width=False, height=True)
        # self.scroll = Tkinter.Scrollbar(self.root).pack(side=Tkinter.RIGHT)
        # TOP
        self.frm = Tkinter.Frame(self.root)
        labelTitle = Tkinter.Label(self.root, text="Data Owner 1", font=("Arial", 26))
        labelTitle.pack()
        # LEFT
        self.frm_l = Tkinter.Frame(self.frm)
        labelControl = Tkinter.Label(self.frm_l, text="Control Panel", font=("Arial", 20), height=2)
        labelControl.pack()
        buttonSetUp = Tkinter.Button(self.frm_l, text="Set Up Connection", font=("Arial", 18), height=2,
                                     command=setUpConnection)
        buttonSetUp.pack(side=Tkinter.LEFT)
        buttonReceiveKey = Tkinter.Button(self.frm_l, text="Receive Public Key", font=("Arial", 18), height=2, command=getKey)
        buttonReceiveKey.pack(side=Tkinter.LEFT)
        self.frm_l.pack(side=Tkinter.TOP)

        self.frm_r = Tkinter.Frame(self.frm)
        buttonEncrypted = Tkinter.Button(self.frm_r, text="Encrypting Original data", font=("Arial", 18), height=2)
        buttonEncrypted.pack(side=Tkinter.LEFT)
        buttonSend = Tkinter.Button(self.frm_r, text="Send to Cloud", font=("Arial", 18), height=2)
        buttonSend.pack(side=Tkinter.LEFT)
        self.frm_r.pack(side=Tkinter.BOTTOM)

        self.frm.pack(side=Tkinter.TOP)

        self.root.mainloop()


def setUpConnection():
    url = 'http://127.0.0.1:4000/'
    sender = 'data_owner_1'
    result = str(set_up_connection(url, sender))
    tkMessageBox.showinfo("Recent Event", result)
    print result


def getKey():
    url = 'http://127.0.0.1:5000/key'
    sender = 'data_owner_1'
    result = send_info(url, sender)
    tkMessageBox.showinfo("Recent Event", result)
    print result


def main():
    db1 = mainFrame()


if __name__ == "__main__":
    main()
