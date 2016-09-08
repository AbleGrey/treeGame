import tkinter as tk
from brTree import *
from PIL import Image, ImageTk



def quitWindow(self):
    self.root.destroy()
def advanceNextDay(self):
    #print(3)
    print('first: ',self.foo.get())
    print('second: ',self.foo2.get())
    print('radio: ',self.rad.get())


    #process allocated resources, weather effects, growth
        #calculate new status, new model, new display
        #clear the selections from prev day, redraw canvas
    
class TreeUI:
    def __init__(self,title,params):
        self.root = tk.Tk()

        fScale = self.fScale = 50
        img = Image.open('images\TreeBranch-2.gif')
        img2 = ImageTk.PhotoImage(img)
    

        #self.root = tk.Tk()
        menubar = tk.Menu(self.root)
        ##submenus
        filemenu = tk.Menu(menubar,tearoff = 0)
        menubar.add_cascade(label = 'File',menu = filemenu)
        filemenu.add_command(label='New',command = lambda:quitWindow(self))
        filemenu.add_command(label = 'Open',command = lambda:quitWindow(self))
        filemenu.add_command(label = 'Save',command = lambda:quitWindow(self))
        filemenu.add_command(label = 'Exit',command = lambda:quitWindow(self))
        ##
        self.root.geometry(str(13*fScale)+'x'+str(8*fScale))
        self.root.config(menu = menubar)

        self.options = tk.LabelFrame(self.root,text = 'Options',width = 4*fScale,height = 5*fScale, bg ='RED')
        self.advisor = tk.LabelFrame(self.root,text = 'Advisor',width = 4*fScale,height = 3*fScale, bg = 'ORANGE')
        self.current = tk.LabelFrame(self.root,text = 'Today is',width = 5*fScale,height = 1*fScale, bg = 'YELLOW')
        self.canvas = tk.Frame(self.root,width = 5*fScale,height = 6*fScale, bg = 'GREEN')
        self.status = tk.LabelFrame(self.root,text = 'Status',width = 5*fScale,height = 1*fScale, bg = 'BLUE')
        self.allocations = tk.LabelFrame(self.root,text = 'Allocate Resources',width = 4*fScale,height = 6*fScale, bg = 'PURPLE')
        self.commit = tk.LabelFrame(self.root,width = 4*fScale,height = 2*fScale)

        col1w = self.options.cget('width')
        col2w = self.status.cget('width')
        self.options.place(x = 0, y = 0)
        self.advisor.place(x = 0, y = self.options.cget('height'))
        self.current.place(x = col1w, y = 0)
        self.canvas.place(x = col1w, y = self.current.cget('height'))
        self.status.place(x = col1w, y = self.current.cget('height')+self.canvas.cget('height'))
        self.allocations.place(x = col1w+col2w, y = 0)
        self.commit.place(x = col1w+col2w, y = self.allocations.cget('height'))


        ##Options Frame Contents
        ##Advisor Frame Contents
        ##Status Frame Contents
        ##Current Frame Contents

        ##Canvas Frame Contents
        self.can = tk.Canvas(master = self.canvas,width = 250,height = 300)
        #topArc = can.create_arc(0,5,250,200, extent = 180, style = tk.ARC)
        topArc = self.can.create_arc(5,5,245,295, start = 0,extent = 180, style = tk.CHORD, fill = 'cyan')
        botArc = self.can.create_arc(5,5,245,295, start = 180,extent = 180, outline = 'green',style = tk.CHORD, fill = 'green')
        topArc = self.can.create_oval(5,5,245,295)# start = 0,extent = 180, style = tk.CHORD)#gndArc = can.create_arc(0,160,250,240,start = 20,extent = 140,style = tk.ARC)
        #trnkPH = can.create_line(125,270,125,170)
        self.mainTree = brTree((125,150),50)

        self.can.pack()

        ##Allocate Frame Contents
            #todo: setup subPanes for clusters of options
        self.foo = tk.IntVar(master = self.root,value = 0)
        self.foo2 = tk.IntVar(master = self.root,value = 0)
        checkSet1 = tk.Checkbutton(master = self.allocations,text = 'first',variable = self.foo, onvalue = 1,offvalue = 0)
        checkSet2 = tk.Checkbutton(master = self.allocations,text = 'second',variable = self.foo2)
        checkSet1.pack(anchor = tk.W,side = tk.TOP)
        checkSet2.pack(anchor = tk.W,side = tk.TOP)
        radioButts = [('All','valueAll'),('Some','valueSome'),('None','valueNone')]
        self.rad = tk.StringVar(master = self.root)
        self.rad.set("Not Set")
        for rText,rMode in radioButts:
            tempButt = tk.Radiobutton(master = self.allocations,text = rText, variable = self.rad, value = rMode)
            tempButt.pack(anchor = tk.W,side = tk.TOP)

        self.pipFrame = tk.Frame(master = self.allocations,width = 200,height = 150)
        self.pipFrame.pack()
        self.pips = [1,2,4]
        self.pipCan = tk.Canvas(master = self.pipFrame,width = 190,height = 100)
        pUp0 = tk.Button(master = self.pipFrame, text = 'Up',command = lambda:self.setPip(0,self.pips[0]+1))
        pUp0.grid(row = 1, column = 0)
        pUp1 = tk.Button(master = self.pipFrame, text = 'Up',command = lambda:self.setPip(1,self.pips[1]+1))
        pUp1.grid(row = 1, column = 1)
        pUp2 = tk.Button(master = self.pipFrame, text = 'Up',command = lambda:self.setPip(2,self.pips[2]+1))
        pUp2.grid(row = 1, column = 2)
        #for pip in range(len(self.pips)):
        self.pipCan.grid(row = 2,columnspan = 3)
        self.drawPips()
        pDown0 = tk.Button(master = self.pipFrame,text = 'Down',command = lambda:self.setPip(0,self.pips[0]-1))
        pDown0.grid(row = 5,column = 0)
        pDown1 = tk.Button(master = self.pipFrame,text = 'Down',command = lambda:self.setPip(1,self.pips[1]-1))
        pDown1.grid(row = 5,column = 1)
        pDown2 = tk.Button(master = self.pipFrame,text = 'Down',command = lambda:self.setPip(2,self.pips[2]-1))
        pDown2.grid(row = 5,column = 2)
        ##Commit Frame Contents
        #img = Image.open(imageFile)
        #img2 = ImageTk.PhotoImage(img)
        #nextDay = tk.Button(master = self.commit, image = img2,command = lambda:advanceNextDay(self), height = 91, width = 191)
        nextDay = tk.Button(master = self.commit, image = img2,command = self.updateBranches, height = 91, width = 191)
        self.image = img2
        #nextDay = tk.Button(master = self.commit,text = 'Next Day', command = lambda:advanceNextDay(self), height = 6, width = 27)
        nextDay.pack()
    def updateBranches(self):
        self.can.delete('branch')
        branches = self.mainTree.reportCoords()
        for coords in branches:
            self.can.create_line(coords,tags='branch')
    def setPip(self,pipId, pipVal):
        self.pips[pipId] = pipVal
        for i in range(len(self.pips)):
            if self.pips[i] < 0:
                self.pips[i] = 0
            if self.pips[i] >=4:
                self.pips[i] = 4
        self.drawPips()
        
    def drawPips(self):
        self.pipCan.delete('pip')
        for i in range(len(self.pips)):
            pip = self.pipCan.create_rectangle(65*i+25,100-25*self.pips[i],35+65*i,100,fill='blue',tags = 'pip')# define pip rectangles
            
        
        
        
    
#root.mainloop()
#dummyRoot = tk.Toplevel()
#img = Image.open('TreeBranch-2.gif')
#img2 = ImageTk.PhotoImage(img)

#sample = treeUI('foop',[1,2])

#sample.root.mainloop()
