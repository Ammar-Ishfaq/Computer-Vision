# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:22:29 2020

@author: M.AMMAR
"""
import tkinter 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from YoloNew import *
import cv2

main_win = tkinter.Tk()
main_win.title('Choose File for the Object Detection')
main_win.geometry("200x200")
main_win.sourceFolder = ''
main_win.sourceFile = ''


def chooseFile():
    txt.delete(0,END)
    main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/", title='Please select a File')
    print(type(main_win.sourceFile ))
    yo=YoloNew(main_win.sourceFile)
    yo.detectIMG()
    txt.insert(INSERT,(yo.get_array_of_objects_name_with_count()))

def chooseCamera():
    ywo=YoloNew()
    ywo.detectVideo()
   
   

b_chooseFile = tkinter.Button(main_win, text = "Chose Picture", width = 20, height = 3, command = chooseFile)
b_chooseFile.grid(row=0,column=0)
b_chooseFile.width = 20

txt=tkinter.Entry(main_win,width=30)
txt.focus()

txt.grid(row=1,column=0)
txt.insert(INSERT, "your count objects list will be here")

b_chooseCamera = tkinter.Button(main_win, text = "Chose Camera", width = 20, height = 3, command = chooseCamera)
b_chooseCamera.grid(row=3,column=0)
b_chooseCamera.width = 20

main_win.mainloop()

