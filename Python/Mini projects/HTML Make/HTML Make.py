# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:33:39 2021

@author: Yusef Quinlan
"""
#tkinter import never needed as interface not implemented in the end.
#from tkinter import *

# Make the initial html text.
text = """  <DOCTYPE HTML1>
            <html>
                <head>
                    <meta charset="utf-8">
                </head>
                <body>
                </body>
            
            </html>
"""

"""
    Function adds tags to the html file until the user no longer wants to add
    tags, any answer other than 'y' will cause the program to think that 'n' has
    been selected.
"""
def addTag():
    global text2
    global text
    global holder

    resp = input(""""What sort of html tag do you want? answer 'h1' for header1,
                 'h2' for a header2 tag, put 'p' for a paragraph tag, or 'a' 
                 for an anchor tag \n""")
    if resp== 'h1':
        texty = input("Please write what you want to add as header text \n")
        text2.insert(holder,"                     " + "<h1>" + texty + "</h1>")
        resp = input("Would you like to add another html tag? answer with y or n \n")
        if resp == 'y':
            holder+=1
            addTag()
    elif resp=='h2':
        texty = input("Please write what you want to add as header text \n")
        text2.insert(holder,"                     " + "<h2>" + texty + "</h2>")
        resp = input("Would you like to add another html tag? answer with y or n \n")
        if resp == 'y':
            holder+=1
            addTag()
    elif resp=='p':
        texty = input("Please write what you want to add as paragraph text. \n")
        text2.insert(holder,"                     " + "<p>" + texty + "</p>")
        resp = input("Would you like to add another html tag? answer with y or n \n")
        if resp == 'y':
            holder+=1
            addTag()
    elif resp=='a':
        url = input("Type in the url: \n")
        atext = input("Type in the text for the hyperlink: \n")
        text2.insert(holder,"                     " + '<a href=' +'"' + url + '">'
                      + atext + "</a>")
        resp = input("Would you like to add another html tag? answer with y or n \n")
        if resp == 'y':
            holder+=1
            addTag()

        

"""
This function can be considered to be the main function, basically it asks the
users what they want the filename of the html file to be called, ask for the 
title of the html file and ask the user if they want to add a html tag. If they
want to add a html tag they will be sent to a function that adds html tags, 
otherwise the file will be created. Anything other than 'y' will be seen as 'n'
"""
def makeHtmlFile():
    global Title
    global fileName
    global Window
    global text2
    global text
    global holder
    Title = input("What will the title of this html file be? \n")
    fileName = input("""What will the filename be? (we add the.html extension)
                   make sure the filename is valid or this will crash. \n""") + ".html"
    text2 = text.splitlines()
    text2.insert(3,"                     " + "<title>" + Title + "</title>")
    holder = 4
    dan = ""
    Resp = input("Would you like to add a html tag? answer with y or n \n")
    if Resp.lower() == 'y':
        addTag()
        for i in text2:
            dan = dan + i + '\n'
        file = open(fileName, "w")
        file.write(dan)
        file.close()
    else:
        for i in text2:
            dan = dan + i + '\n'
        file = open(fileName, "w")
        file.write(dan)
        file.close()
        
        
        
    """
    Window = Tk()
    Window.title(fileName)
    F = Frame(Window)
    Label1 = Label(Window, text="The next label shows the current html").pack()
    Label2= Label(Window, text="").pack()
    Label3= Label(Window, text=dan).pack()
    Sidescroll = Scrollbar(Frame)
    Sidescroll.pack(side=RIGHT, fill='y')
    Horiscroll = Scrollbar(Frame, orient=HORIZONTAL)
    Horiscroll.pack(side=BOTTOM, fill='x')
    Sidescroll.config(command = Frame.xview)
    Horiscroll.config(command = Frame.yview)
    Window.mainloop()
    """
    
makeHtmlFile()