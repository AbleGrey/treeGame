import tkinter as tk
import functools as ft #only need this for partial() in lieu of lambda
    #given that lambdas aren't viable for a dynamic function with dynamic args

class msgQuest:
    #class of custom button box dialog windows
    def __init__(self,parent,msg,buttonDict = {}):
        #initialize with the following:
            #parent, some tk.<thing> object
            #message text, a string which will be displayed in the window
            #dictionary of buttons
                #format: {button label string: callback function name}
        self.top = tk.Toplevel(parent)
            #sets the toplevel dialog box window
        self.title = 'Select'
            #sets the window title
            #todo: decide whether this should be an __init__ arg or not
        self.message = msg
            #sets the message text
        tk.Label(self.top,text = self.message).pack()
            #packs the message text as a Label object
        for buttonName in buttonDict.keys():
            #go through optional __init__ button dictionary and add buttons 
            tk.Button(self.top,text = buttonName,command = ft.partial(buttonDict[buttonName],self.top)).pack(side = tk.LEFT)
                #totally optional
    def addButton(self,txt,funct):
        tk.Button(self.top,text = txt, command = ft.partial(funct,self.top)).pack(side = tk.LEFT)
            #method to add a button to the dialog window and define the callback
    #todo: add some methods to add some image alongside the text & buttons
