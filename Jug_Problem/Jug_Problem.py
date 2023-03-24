#Also in "How to Run.txt"
#I have attached the python main function at very bottom (how it should be normally ran)
#it will create an assignment class and run the following functions
#if you wish to alter test cases you can do so under def testCase(self)
#There should be no issue running this IF u are using the updated python 3


class Assignment1:
    currentState = ()
    capacity = (5,2)
    initialState = (4,1)
    goalState = (0,1)
    path = []
    actions = []

    def __init__(self,initialState=initialState, goalState= goalState, capacity=capacity):
        self.initialState = initialState
        self.goalState = goalState
        self.capacity = capacity
        self.currentState = self.initialState
    
        

    def testCase(self):

        #test #1
        self.capacity = (5,2)
        self.initialState= (4,1)
        self.goalState =(0,1)
        self.currentState = self.initialState

        ret= self.printAll()

        #test #2
        self.capacity = (5,2)
        self.initialState=(4,1)
        self.goalState=(4,0)
        self.currentState = self.initialState

        ret+= self.printAll()

        #test #3
        self.capacity = (5,2)
        self.initialState=(4,1)
        self.goalState=(5,0)
        self.currentState = self.initialState

        ret+= self.printAll()

        #test #4
        self.capacity = (5,2)
        self.initialState=(4,1)
        self.goalState=(3,2)
        self.currentState = self.initialState

        ret+= self.printAll()

        #test #5
        self.capacity = (5,2)
        self.initialState=(4,1)
        self.goalState=(1,2)
        self.currentState = self.initialState

        ret+= self.printAll()

        with open('output.txt', 'w') as f:
            f.write(ret)

    def printAll(self,):
        ret = self.printBFS()
        ret+="\n\n\n\n"
        ret += self.printDFS()
        ret+="\n\n\n\n"
        ret += self.printAstar()
        ret+="\n\n\n\n"
        return ret



    def printAstar(self):
        self.currentState = self.initialState
        #used for easier writing
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}
        ret = "Initial State :"+ str(self.initialState)+" \nGoal state: "+str(self.goalState)+" \n"
        ret+= "Searching strategy: Astar \n"
        temp = self.Astar()
        if temp is not None:
            Action = str(temp[2])
            #this is what happens if u dont read prompt first we have to include the traversed path
            Action = Action[len("(initial)"):]
            ret += "Path:"+str(self.currentState)
            while len(Action) != 0:
                function = Action[0:len("(dump1)")]
                Action = Action[len("(dump1)"):]
                for x in action:
                    if (action[x] == function):
                        self.currentState =  value[x](self.currentState)
                        ret += str(self.currentState) + " "
                    
            ret+="\n"
            Action = str(temp[2])[len("(initial)"):]
            ret+="Action: "+Action+"\n"
            ret+="Cost: " + str(len(Action.split(")("))) 
        
        else:
            ret += "Path: Too many steps or impossible goal state"
        return ret

    def printDFS(self):
        self.currentState = self.initialState
        #used for easier writing
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}
        ret = "Initial State :"+ str(self.initialState)+" \nGoal state: "+str(self.goalState)+" \n"
        ret+= "Searching strategy: DFS \n"
        temp = self.DFS()
        if temp is not None:
            Action = str(temp[2])
            #this is what happens if u dont read prompt first we have to include the traversed path
            Action = Action[len("(initial)"):]
            ret += "Path:"+str(self.currentState)
            
            while len(Action) != 0:
                function = Action[0:len("(dump1)")]
                Action = Action[len("(dump1)"):]
                for x in action:
                    if (action[x] == function):
                        self.currentState = value[x](self.currentState)
                        ret += str(self.currentState) + " "
                    
            ret+="\n"
            Action = str(temp[2])[len("(initial)"):]
            ret+="Action: "+Action+"\n"
            ret+="Cost: " + str(len(Action.split(")("))) 
        
        else:
            ret += "Path: Too many steps or impossible goal state"
        return ret
    def printBFS(self):
        self.currentState = self.initialState
        #used for easier writing
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}
        ret = "Initial State :"+ str(self.initialState)+" \nGoal state: "+str(self.goalState)+" \n"
        ret+= "Searching strategy: BFS \n"
        temp = self.BFS()
        if temp is not None:
            Action = str(temp[2])
            #this is what happens if u dont read prompt first we have to include the traversed path
            Action = Action[len("(initial)"):]
            ret += "Path:"+str(self.currentState)
            while len(Action) != 0:
                function = Action[0:len("(dump1)")]
                Action = Action[len("(dump1)"):]
                for x in action:
                    if (action[x] == function):
                        self.currentState =  value[x](self.currentState)
                        ret += str(self.currentState) + " "
                    
            ret+="\n"
            Action = str(temp[2])[len("(initial)"):]
            ret+="Action: "+Action+"\n"
            ret+="Cost: " + str(len(Action.split(")("))) 
        
        else:
            ret += "Path: Too many steps or impossible goal state"

        return ret
        
    #BFS search
    def BFS(self,temp=[(initialState[0],initialState[1],"(initial)")], nodesDeep = 0, maxDepth = 500):
        #temp will be a list containing tuples [(state0,state1,actions)]

        if(nodesDeep>=maxDepth):
            return None

        #easier to read sets
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}

        #first we check all possible moves and add it to the list
        for x in range(4):
            
            #temp1 will store returning function call
            temp1 = value[x]((temp[0][0],temp[0][1]))

            if temp1 is not None:
                    
                #reorganize to (state0,state1,action)
                temp1 = (temp1[0],temp1[1],temp[0][2]+action[x])

                #we have found our goal
                if ((temp1[0],temp1[1]) == self.goalState):
                    return temp1
                #added
                temp.append(temp1)

        
        #we have not found any traversals from first so we remove and continue
        temp.pop(0)

        #we have parsed all possibilities no path found
        if(len(temp) == 0 ): return None

        return self.BFS(temp,nodesDeep+1,maxDepth)



    

    #DFS search
    def DFS(self,temp=[(initialState[0],initialState[1],"(initial)")], nodesDeep=0,maxDepth = 500):
        #temp will be a list containing tuples [(state0,state1,actions)]
        #nodesDeep is to prevent going to deep u can change max Depth accordingly
        if(nodesDeep>=maxDepth):
            return None
        if(temp==None or len(temp) == 0):
            return None
            

        #easier to read sets
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}
        
        #first we check all possible moves and add it to the list
        for x in range(4):

            #temp1 will store returning function call
            temp1 = value[x]((temp[0][0],temp[0][1]))

            if temp1 is not None:
                    
                #reorganize to (state0,state1,action)
                temp1 = (temp1[0],temp1[1],temp[0][2]+action[x])

                #we have found our goal
                if (temp1[0] == self.goalState[0] and temp1[1] == self.goalState[1]):
                    return temp1

                #not found so we can ignore
                elif(temp1==None):
                    continue
                
                #added to end of list
                temp.append(temp1)

                #attempt to go deeper into node
                return self.DFS(temp,nodesDeep+1, maxDepth)

        #we have traversed all possible nodes for this we now remove this node
        temp.pop(0)

        #removed and now we go back a step and backtrack
        return self.DFS(temp,nodesDeep+1, maxDepth)
        
        

        
    #Astar search
    def Astar(self,temp = (initialState[0],initialState[1],"(initial)"),heuristicValues={}, nodesDeep = 0, maxDepth = 500):
        #temp will be a list containing tuples [(state0,state1,actions)]

        if(nodesDeep>=maxDepth):
            return None
        if(temp == None):
            return None
            

        #easier to read sets
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        value = {0:self.pour1,1:self.pour2,2:self.dump1,3:self.dump2}
        
        #first we check all possible moves and add it to the list
        for x in range(4):

            #temp1 will store returning function call
            temp1 = value[x]((temp[0],temp[1]))

            if temp1 is not None:

                #added to heuristic values
                hVal = self.heirusticFunct((temp1[0],temp1[1],temp[2]),action[x])

                #reorganize to (state0,state1,action)
                temp1 = (temp1[0],temp1[1],temp[2]+action[x])

                if hVal == 0:
                    return temp1

                #adding heuristic value of it to the dict
                if hVal in heuristicValues:
                    heuristicValues[hVal].insert(0,temp1)
                else:
                    heuristicValues[hVal] = [temp1]

        if(len(heuristicValues)==0):
            return None

        #find lowest heuristic Value
        ret = min(heuristicValues.keys())

        #will get lowest heuristic state
        temp = heuristicValues[ret][0]


        if(len(heuristicValues[ret]) == 0):
            del heuristicValues[ret]
        else:
            heuristicValues[ret].pop(0)
            if(len(heuristicValues[ret]) == 0):
                del heuristicValues[ret]

        #there is no possible way of hitting node
        if(len(heuristicValues.keys())==0):
            return None

        return self.Astar(temp,heuristicValues,nodesDeep+1,maxDepth)
    #will return an integer for most desired state
    def heirusticFunct(self,state=(),nextAction=""):


        #if path we are checking is already the goal state
        if(state[0]==self.goalState[0] and state[1]==self.goalState[1]):
            return 0

        #we do not want to have repeated actions so if we see a repeat we will consider it impossible
        action = {0:"(pour1)",1:"(pour2)",2:"(dump1)",3:"(dump2)"}
        lastAction = str(state[2])
        lastAction = lastAction[len(lastAction)-7:]
       
        #repeated action
        if(lastAction == nextAction):
            return 100


        #subtracted too much we cannot reach goal from here
        if (state[0]+state[1] < self.goalState[0]+self.goalState[1]):
            return 100

        #we can only go to states
        #(r+k*cs2,0 or cs2) 
        #where r = remainder of gs1%cs2
        #k = some whole number
        #cs2 = capacity of jug 2
        #if it is anything else we cannot reach it
        

        #checking if GS1 is a possible state
        remainder = (self.initialState[0]+self.initialState[1])%self.capacity[1]
        if(self.goalState[0]==remainder and (self.goalState[1] == 0 or self.goalState[1]==self.capacity[1])):
            #weighs favorably towards pour1 and dump2
            if(nextAction == action[0] or nextAction == action[3]):
                return 2

        #checking if GS2 is a possible state
        remainder = self.initialState[0]%self.capacity[1]
        if(self.goalState[1]==remainder and (self.goalState[0] == 0 or self.goalState[0]==self.capacity[1])):
            #weighs favorably towards pour1 and dump2
            if(nextAction == action[0] or nextAction == action[3]):
                return 2

        if(self.goalState[0] == 0 and self.goalState[1] == 0):
            if(nextAction == action[2] or nextAction == action[3]):
                return 2

        #if it is not either of the above we just increase weight to last possible decision
        return 50
        

    #transferring from 1 to 2
    #returns None or a new state (pair)
    def pour1(self,state=()):

        if(state==() or state == None):
            return None

        ret0 = state[0]
        ret1 = state[1]

        #2 is already full
        if (state[1] == self.capacity[1]):
            return None

        #1 is already empty
        elif(state[0] == 0):
            return None
        
        #space left in jug2 to get filled
        difference = self.capacity[1]-ret1
        
        #we are transferring whats left of jug 1
        if(difference>ret0):
            ret1= ret1+ret0
            ret0 = 0

        #we are transferring some of jug1
        else:
            ret1= ret1+difference
            ret0= ret0-difference

        return (ret0,ret1)

    #transferring from 2->1
    def pour2(self,state=()):

        if(state==() or state==None):
            return None

        ret0 = state[0]
        ret1 = state[1]
        #1 is already full
        if (state[0] == self.capacity[0]):
            return None

        #2 is already empty
        elif(state[1] == 0):
            return None
        
        #space left in jug1 to get filled
        difference = self.capacity[0]-ret0
        
        #we are transferring whats left of jug 2
        if(difference>ret1):
            ret0+=ret1
            ret1 = 0

        #we are transferring some of jug2->1
        else:
            ret0+=difference
            ret1-=difference

        return (ret0,ret1)

    #dump whatever is in 1 will return None if its already empty
    def dump1(self,state=currentState):
        if(state[0]==0):return None
        return (0,state[1])

    #dump whatever is in 2 will return None if it is already empty
    def dump2(self,state=currentState):
        if(state[1]==0):return None
        return (state[0],0)

if __name__ == "__main__":
    start = Assignment1()
    start.testCase()