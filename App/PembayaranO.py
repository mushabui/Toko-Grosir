#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 12, 2020 11:45:47 PM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import PembayaranO_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    PembayaranO_support.set_Tk_var()
    top = Pembayaran (root)
    PembayaranO_support.init(root, top)
    root.mainloop()

w = None
def create_Pembayaran(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Pembayaran(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    PembayaranO_support.set_Tk_var()
    top = Pembayaran (w)
    PembayaranO_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Pembayaran():
    global w
    w.destroy()
    w = None

class Pembayaran:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("398x450+339+201")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("GROCERYBOX")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.089, height=21, width=84)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Jumlah Order''')

        self.Spinbox1 = tk.Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.302, rely=0.089, relheight=0.042
                , relwidth=0.264)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=PembayaranO_support.spinbox)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.05, rely=0.178, height=21, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Jumlah Bayar''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.302, rely=0.178,height=20, relwidth=0.261)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.05, rely=0.267, relheight=0.584
                , relwidth=0.402)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Pembayaran dapat melalui:
BCA - 9083218891
a.n Asep Sunandar
MANDIRI - 990891889217
a.n Asep Sunandar
BRI - 3900008287329218
a.n Asep Sunandar
BNI - 709878287
a.n Asep Sunandar

Konfirmasi Pembayaran
WA - 082137760998
a.n Asep Sunandar''')
        self.Message1.configure(width=160)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.678, rely=0.844, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Quit''')
        self.Button1.bind('<Button-1>',lambda e:PembayaranO_support.QuitButton(e))

if __name__ == '__main__':
    vp_start_gui()





