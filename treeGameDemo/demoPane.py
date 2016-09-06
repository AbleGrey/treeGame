##Imports
import tkinter as tk #use this for all the GUI elements
from brTree import * #use this for the tree model handling
from msgQuest import * #customizable button-box prompts
import PIL
from PIL import Image, ImageTk


##Parameters
artAssetDir = 'images'
canvasW = 500
canvasH = 500 #canvas dimensions for the tree figure
trunkLength = canvasH/3 #scale the tree trunk to the canvas dimensions
initialDensity = 3 #number of branches per fork of the tree
initialDepth = 4 #initial depth of the tree

##Helper functions
def GrowTall(tree):
    #input: brTree object instance
    #output: modifies the named brTree to increase brTree.depth by +1
        #also redraws the canvas, based on modified tree
    tree.setDepth(tree.depth+1)
    updateDrawing(tree)
    
def GrowDense(tree):
    #input: brTree object instance
    #output: modifies the named brTree to increase brTree.density by +1
        #also redraws the canvas, based on modified tree
    tree.setDensity(tree.density+1)
    updateDrawing(tree)
    
def New():
    #placeholder, button example for Question Message button dialog
    quest = msgQuest(root,'A, B, or C')
    quest.addButton('option A',clickA)
    quest.addButton('option B',clickB)
    quest.addButton('option C',clickC)
    
def quitWindow():
    #quits out of whole tkinter window
    root.destroy()
    
def Reset(tree):
    #input: brTree object instance
    #output: modifies the named brTree to return to initial values
        #also redraws the canvas, based on modified tree
    tree.setDensity(initialDensity)
    tree.setDepth(initialDepth)
        #todo: move this initial value/default into the brTree class def
    updateDrawing(tree)
    
def updateDrawing(tree):
    #redraws the canvas, based on modified tree
    can.delete('all')
        #delete all current items on canvas
    treeLines = tree.reportCoords()
        #call the tree's coordinate report
            #report format is a list of ((x1,y1),(x2,y2)) tuples
    for coords in treeLines:
        #for each set of coordinates, add an element at those coordinates
        can.create_line(coords, tags = 'branch')
            #todo: alter line width proportional to branch length
                #or just change the element type to represent a branch
            #'branch' tag will be used later for click-detection
            #todo: add some other tags as needed to distinguish objects
        
def Advance():
    #placeholder function called by 'FIRE' button
    print('next day')
    
def clickA(button):
    #placeholder function called by button sample
    print('A clicked')
    button.destroy()
    
def clickB(button):
    #placeholder function called by button sample
    print('B clicked')
    button.destroy()
    
def clickC(button):
    #placeholder function called by button sample
    print('C clicked')
    button.destroy()
    
def onWidgetClick(event):
    #widget click event callback
    #note that event.widget refers to the canvas object
    widgID = event.widget.find_closest(event.x,event.y)
        #call up the handles for the clicked element
    curWidgWidth = event.widget.itemcget(widgID,'width')
        #call up the value for the 'width' property of the target widget
    event.widget.itemconfig(widgID,width = float(curWidgWidth)+5)
        #update the 'width' property of the target widget
    #todo: handle multiple stacked, clickable objects

##Pane and UI objects definition
root = tk.Tk()
    #instantiate the base tkinter pane/frame
menubar = tk.Menu(root)
    #define the Menu that will be used to list the top level menu bar object
filemenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu = filemenu)
    #subMenu placeholder for 'file' options
filemenu.add_command(label='New',command = New)
filemenu.add_command(label = 'Open',command = lambda:Reset(someTree))
filemenu.add_command(label = 'Save',command = lambda:Reset(someTree))
filemenu.add_command(label = 'Exit',command = quitWindow)
    #filemenu command placeholders
    #todo: implement file save features

treemenu = tk.Menu(menubar,tearoff = 0)
    #subMenu containing tree parameter modifying calls
menubar.add_cascade(label = 'Tree',menu = treemenu)
treemenu.add_command(label='Taller!',command = lambda:GrowTall(someTree))
treemenu.add_command(label = 'Denser!',command = lambda:GrowDense(someTree))
treemenu.add_command(label = 'Reset',command = lambda:Reset(someTree))

#MAKE ANY MENUBAR LAYOUT UPDATES BEFORE THIS
root.config(menu = menubar)
    #sets the menubar for the frame

##Some more placeholder UI elements
fireButton = tk.Button(text = 'FIRE',command = Advance)
fireButton.pack(fill = tk.X,side = tk.BOTTOM)
    #placeholder, sample button on the frame itself
    #note the 'fill' = X option set to max out the button width

##Define the Canvas
someTree = brTree((canvasW/2,canvasH),trunkLength,initialDepth,initialDensity)
    #instantiate a tree to call for the canvas
can = tk.Canvas(root, width = canvasW, height = canvasH)
    #define the canvas object in which to draw the tree
    #note that the canvas itself cannot be assigned tags
updateDrawing(someTree)
    #perform the initial draw for the tree with default dimensions
can.tag_bind('branch', '<ButtonPress-1>', onWidgetClick)
    #whenever a canvas element with the tag 'branch' is clicked,
    #call the onWidgetClick function
can.pack(side = tk.TOP)
    #todo: settle on pack() vs grid() for element layout
    #pack is simpler if we only need a few elements,
    #but grid affords more control
img = Image.open(artAssetDir+'\TreeBranch-1.gif')
basewidth = 200
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img = img.convert('RGBA')
rot = img.rotate(270, expand = 1)
fff = Image.new('RGBA', rot.size, 0x000000FF)
out = Image.composite(rot, fff, rot)
tkimg = ImageTk.PhotoImage(out)
can.create_image(100, 200, image=tkimg)


##Put it all together
root.mainloop()
    #actually runs the main pane
