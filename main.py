from pyhooked import Hook, KeyboardEvent, MouseEvent
import pyautogui
import threading
import tkinter

import sys


now_key = "r"
now_key_code = 82
stop_key = "g"
stop_key_code = 71
click_num = 30
nowco = 0

enp = None
a = None
exit_flg = False
change_click_flg = False
change_lock_flg = False
def handle_events(args):
    global nowco,stop_key_code,now_key_code,click_num
    if exit_flg:
        exit()
    if isinstance(args, KeyboardEvent):
        # print(args.key_code)

        if args.key_code == now_key_code:
            # print(click_num)
            for i in range(click_num):
                # print(nowco)
                if nowco == 0:
                    # print("rtesat")
                    pyautogui.click()
                    
                    # pyautogui.rightClick()
def lock_event(args):
    global nowco
    if exit_flg:
        exit()
    if isinstance(args, KeyboardEvent):
        if args.key_code == stop_key_code:
            # print("koko")
            
            if nowco == 1:
                nowco = 0
            elif nowco == 0:
                nowco = 1
def click_lock():
    hk = Hook()  # make a new instance of PyHooked
    hk.handler = lock_event  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
    hk.hook() 
    
            
    
def check_key():
    hk = Hook()  # make a new instance of PyHooked
    hk.handler = handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
    hk.hook()
    
def change_click_num():
    global click_num,enp
    click_num = int(enp.get())
    # print(click_num)
    # enp.delete(0, tkinter.END)
    enp.insert(tkinter.END,click_num)
    
def end_thread():
    global a,exit_flg
    exit_flg = True
    a.destroy()


def set_window():
    global enp,a
    a = tkinter.Tk()
    a.title("auto clicker")
    a.geometry("400x400")
    
    set_key_button = tkinter.Button(text="変更")
    set_lock_key = tkinter.Button(text="変更")
    set_click_num = tkinter.Button(text="変更", command=change_click_num)
    
    enp = tkinter.Entry(width=23)
    lavel1 = tkinter.Label(text="クリック回数")
    lavel2 = tkinter.Label(text="連打キー")
    lavel3 = tkinter.Label(text="連打ロック")
    lavel4 = tkinter.Label(text="r")
    lavel5 = tkinter.Label(text="g")
    
    lavel1.place(x=60,y=100)
    lavel2.place(x=60,y=140)
    lavel3.place(x=60,y=180)
    lavel4.place(x=190,y=140)
    lavel5.place(x=190,y=180)
    
    enp.place(x=140,y=100)
    enp.insert(tkinter.END,click_num)
    # set_key_button.place(x=290,y=140)
    # set_lock_key.place(x=290,y=180)
    set_click_num.place(x=290,y=97)
    a.protocol("WM_DELETE_WINDOW", end_thread)
    a.mainloop()
    
set_window_thread = threading.Thread(target=set_window)
check_key_thread = threading.Thread(target=check_key)
check_lock_thread = threading.Thread(target=click_lock)
set_window_thread.start()
check_key_thread.start()
check_lock_thread.start()
set_window_thread.join()
