

#just some const set to use as a reference
reference = frozenset({'1','2','3','4','5','6','7','8','9'})

#main loop to run stuff
def run():
    
    #do-while loop to display menu
    cont = True
    while(cont):

        print('Your sudoku grid must:\n-Be a continuous string of 81 characters\n-A empty space is marked with a \'.\'\nWhat is your string?')
        grid = input()

        #FOR GRADER USE:
        
        #for AC3 use:
        #result = AC3(grid)

        #for MCV use:
        result = AC3(grid,MCV=True)

        #for LCV use:
        #result = AC3(grid,LCV=True)

        #will display results in readable format
        if result!="":
            print('\n\nResults:\n')
            displayGrid(result)
        else:
            print ("not possible")
        
        #ask for continuation
        print('\n\nWould you like to continue(Y/N)')
        cont = False if input()=='N' else True

#using AC3
#Constraints for recursive call
#MCV and LCV are disabled by default and enbaled during runtime
def AC3(grid, constraints=None, MCV=False,LCV=False):

    if(len(grid)!=81):
        print("Eror missing numbers")
        return False

    #gathers constraints for arc consistency
    if (constraints == None):
        constraints = getConstraints(grid)
    
    #sets MCV or LCV enabled
    if(MCV):
        constraints.sort(key=getLength)
    elif(LCV):
        constraints.sort(key=getLength,reverse=True)


    #for loop to go thru AC3
    for i,j in constraints:

        #changes that index to next available in set
        if(grid [i] =='.'):
            
            #goes through all possibilities
            for k in j:

                grid = grid[:i]+str(k)+grid[i+1:]

                temp = reduceDomain(grid,i,constraints)

                #if possible we find next possibility
                if temp != None:

                    #sucessfully returned
                    ret = AC3(grid,temp)

                    #we have found a result
                    if(ret!=""):
                        return ret

            #we have exhausted all possibilities it is impossible from here
            return ""

    #sucessfully solved returning string
    return grid


#this will get all the domains and reduce the set(s) based off of what was added in position
def reduceDomain(grid,pos,constraints):

    #number to remove
    remove = grid[pos]

    #set to return
    ret = []

    #deep copy
    for i,j in constraints:
        temp = set()
        for k in j:
            temp.add(k)
        ret.append((i,temp))

    #gets all row domain
    for i in range((pos//9)*9,(pos//9)*9+9):
        
        #going thru constraints in pair (index,set of possibilities)
        for j,k in ret:
            
            #finds row index
            if j == i:
                
                #remove possibility if it exists
                if remove in k:
                    k.discard(remove)

                    #Not arc consistent
                    if len(k) == 0 and grid[i]=='.':
                        return None
                
    #checks column
    for i in range((pos%9),81,9):
        
        #going thru constraints in pair (index,set of possibilities)
        for j,k in ret:
            
            #finds row index
            if j == i:
                
                #remove possibility if it exists
                if remove in k:
                    k.discard(remove)

                    #Not arc consistent
                    if len(k) == 0 and grid[i]=='.':
                        return None
    
    
    #row/col will store the position of the top left most digit from the 3x3 grid
    rowg = (pos//27)*3
    colg = ((pos%9)//3)*3

    #gets all grid numbers/values
    for x in range (3):
        for y in range(3):

            #going thru constraints in pair (index,set of possibilities)
            for j,k in ret:
            
                #finds row index
                if j == (rowg*9)+colg+(x*9)+y:
                
                    #remove possibility if it exists
                    if remove in k:
                        k.discard(remove)

                        #Not arc consistent
                        if len(k) == 0 and grid[i]=='.':
                            return None


    return ret

#will order from lowest # of possibilities to highest
def getConstraints(grid):
    #list containing a pair for index and constraints (index:#ofConstraints)
    constraints =[]
    for i in range(81):

        #adds constraints to unknowns
        constraints.append((i,get(grid,i)))
        
    return constraints

#throwaway function for sort
def getLength(pair):
    return len(pair[1])


#create check functions that will check the row,col,grid to see if each value is valid

#will return a set of all possibilities that the position can be (including the number it is already)
#mainly used for MCV and LCV
def get(str1,pos):    
    return getRow(str1,pos).intersection(getCol(str1,pos),getGrid(str1,pos))


#return set of possibilities that pos can be based off of the row
def getRow(str, pos):
    
    #stores numbers 1-9 in a set called ret
    ret = set()
    for x in reference:
        ret.add(x)
 
    #rounding the position of the number of concern
    num = (pos//9)*9

    #grabbing entire row
    row = str[num:num+9]

    #discarding any numbers already existing in the row
    for x in row:
        if x in ret:
            ret.discard(x)

    #adds back in the current number
    if str[pos] != '.':
        ret.add(str[pos])

    return ret

#return set of possibilities that pos can be based off of the col
def getCol(str, pos):

    ret = set()
    for x in reference:
        ret.add(x)

    #number of reference for columns
    num = pos%9

    #grabs entire column
    col = ""
    for x in range(0,81,9):
        col+=str[x+num]
    
    #discards any numbers already existing
    for x in col:
        if x in ret:
            ret.discard(x)
    
    #adds back in the current number
    if str[pos] != '.':
        ret.add(str[pos])

    return ret
    
#return set of possibilities that pos can be based off of the 3x3 grid
def getGrid(str, pos):

    ret = set()
    for x in reference:
        ret.add(x)

    #row/col will store the position of the top left most digit from the 3x3 grid
    rowg = (pos//27)*3
    colg = ((pos%9)//3)*3

    #finds numbers in row, discards any existing ones
    char = ""
    for x in range (3):
        for y in range(3):
            char+=str[(rowg*9)+colg+(x*9)+y] #crazy math to get position
    
    #checks all numbers we've gotten and compares
    for x in char:
        if x in ret:
            ret.discard(char)

    #adds back in the current number
    if str[pos] != '.':
        ret.add(str[pos])   
    
    return ret

#For debugging/displaying results of grid
def displayGrid(grid):
    for col in range(0,9):
        temp = ""
        
        #splits into 3 sections
        temp = grid[col*9:col*9+3] + "|" + grid[col*9+3:col*9+6] + "|" + grid[col*9+6:col*9+9]

        if col%3==0 and col != 0: 
            print('-'*12)

        print(temp)
        

#just a main function to keepy it simple
if __name__ == "__main__":
    run()