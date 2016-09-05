##Imports
import math #used for some trig calls on branch angles, lengths

#Parameters
branchScaleFactor = 0.6
    #ratio of child to parent branch lengths

class brTree:
    #placeholder Tree model, from fractals homework w/uniform forks/node
    #note that this tree grows upward, in the -Y direction
    def __init__(self,branchOrigin,branchLen,depth,density):
        #initialized with the following:
            #trunk origin coordinate, (x,y) tuple
            #trunk length, float
            #tree depth, int number of generations of child branches
            #branch density, int number of children per forking node
        self.brL = branchLen
        self.brC = branchOrigin
        self.depth = depth
        self.density = density
        self.updateModel()
                
    def setDepth(self,newDepth):
        #adjust tree depth
        self.depth = newDepth
        
    def setDensity(self,newDensity):
        #adjust tree density
        self.density = newDensity
        
    def updateModel(self):
        #store latest whole-tree model
        #todo: optimize updates to this model to avoid recalculating
            #the whole thing from scratch upon each update
        trunkDict = {'origin':self.brC,'length':self.brL,'angle':math.pi/2,'kids':[]}
            #dictionary describing the base, childless "trunk" branch
        self.model = addChildren(trunkDict,self.density,self.depth,1)
            #build model from the initial trunk with the current params
            
    def reportCoords(self):
    #report branch coordinates in format:
            #list of x/y tuple pairs [ ((X1,Y1),(X2,Y2)), ..., ((X1,Y1),(X2,Y2)) ]
        self.updateModel()
            #update the Model, in case params have changed 
        return parseModel(self.model)
            #parse out x/y tuples from {origin,length,angle} dictionaries
    
##Helper functions
def parseModel(treeModelDict):
    #
    parentLength = treeModelDict['length']
    parentOriginX =treeModelDict['origin'][0]
    parentOriginY = treeModelDict['origin'][1]
    parentAngle = treeModelDict['angle']
        #pull out all the parent's parameters
    childOriginX = parentOriginX+parentLength*math.cos(parentAngle)
    childOriginY = parentOriginY-parentLength*math.sin(parentAngle)
        #calculate child origin/parent terminus coordinates
    output = [((parentOriginX,parentOriginY),(childOriginX,childOriginY))]
    for i in treeModelDict['kids']:
        #iterate over each child branch and concatenate the results
        output += parseModel(i)
    return output
    
def addChildren(treeModelDict,density,depthMax,depthCur):
    #recursively add children to the model described by treeModelDict-
        #until target density and depth are reached
        #depthCur describes the current level of depth per iteration
    output = treeModelDict
    if depthMax == depthCur:
        #base case, maximum depth reached in current iteration
        return treeModelDict
    for i in range(density):
        parentLength = treeModelDict['length']
        parentOriginX =treeModelDict['origin'][0]
        parentOriginY = treeModelDict['origin'][1]
        parentAngle = treeModelDict['angle']
            #pull out all the parent's parameters
        childOriginX = parentOriginX+parentLength*math.cos(parentAngle)
        childOriginY = parentOriginY-parentLength*math.sin(parentAngle)
        childLength = parentLength*branchScaleFactor
        childAngle = parentAngle-math.pi/2 + (i+1)*(math.pi/(density+1))
            #compute all the new child's parameters
            #note the use of (i+1) scalar to space branches evenly,
                #fanned to evenly divide the surrounding 180 degree arc
        tempDict = {'origin':(childOriginX,childOriginY),'length':childLength,'angle':childAngle,'kids':[]}
            #a temporary branch dictionary to host the new child,
                #while we recurse for the grandchild generation
        output['kids']+=[addChildren(tempDict,density,depthMax,depthCur+1)]
    return output
