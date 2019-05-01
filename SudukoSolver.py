#A suduko Solver made using a backtracking algorithm 


#This fucntions finds unfilled boxed withtin the Suduko       
def FindUnfilled(puzz,temp): 
    

    for r in range(0,9,1): 
        
        for c in range(0,9,1): 
            #If a box is 0 it is empty
            if(puzz[r][c]==0): 
                
                #Positions are set
                temp[0]=r
                temp[1]=c 

                return True
    return False
  

#This function determines if test value is already present in the row
def IsInRow(puzz,row,test): 
    
    for i in range(0,9,1): 
        #Tests each number in row with the value
        if(puzz[row][i] == test):     
            return False
    return True
  
#Determines if the test value is already present within the colunm
def IsInCol(puzz,col,test): 
    
    for i in range(0,9,1): 
        if(puzz[i][col] == test): 
            
            return False
    return True
  
#Checks if test value is present within the box
def IsInBox(puzz,row,col,test): 
    
    for x in range(0,3,1): 
        
        for y in range(0,3,1): 
            #Subtracting modulus of row and colunm determines the location of the bottom left box. This prevents indexing out of bounds. 
            if(puzz[x+(row-row%3)][y+(col-col%3)] == test): 
                return False
    return True 

#Main function for solving the puzzle
def Solve(puzz): 
    
    #Temp location variable is created   
    temp=[0,0] 
     
    #Finds empty spaces  
    if(not FindUnfilled(puzz,temp)): 
        return True
      
    #Stores the locations
    row=temp[0] 
    col=temp[1] 
      
    # Cycles through each value to test if it will work in the location
    for test in range(1,10,1): 

        #Checks if it is possible to place the value in the location
        if(IsInRow(puzz,row,test) and IsInCol(puzz,col,test) and IsInBox(puzz,row,col,test)):  
            
            #Places the given value on the grid  
            puzz[row][col]=test 
  
            #Resources I used to learn about back tracking 
            # https://medium.com/@andreaiacono/backtracking-explained-7450d6ef9e1a
            # https://www.geeksforgeeks.org/backtracking-introduction/
            # NO ACTUAL CODE WAS COPIED 


            #Backtracks using recursion to solve the puzzle
            if(Solve(puzz)): 
                return True
  
            #If value does not end up working, location is changed back to 0
            puzz[row][col] = 0

    return False 
  
#Function to display the solved puzzle.
def DisplayGrid(puzz): 
    for i in range(0,9,1): 
        print (puzz[i]) 

#Takes input for all 9 lines of the suduko, 0's are empty spaces 
print("Welcome to a Suduko Solver. Please enter the puzzle row by row, replacing blank spaces with 0's")
r1 = list(map(int, (input("Enter numbers in the first row, if box is blank use 0: "))))
r2 = list(map(int, (input("Enter numbers in the second row, if box is blank use 0: "))))
r3 = list(map(int, (input("Enter numbers in the third row, if box is blank use 0: "))))
r4 = list(map(int, (input("Enter numbers in the fourth row, if box is blank use 0: "))))
r5 = list(map(int, (input("Enter numbers in the fith row, if box is blank use 0: "))))
r6 = list(map(int, (input("Enter numbers in the sixth row, if box is blank use 0: "))))
r7 = list(map(int, (input("Enter numbers in the seventh row, if box is blank use 0: "))))
r8 = list(map(int, (input("Enter numbers in the eigth row, if box is blank use 0: "))))
r9 = list(map(int, (input("Enter numbers in the ninth row, if box is blank use 0: "))))


#Combines into a 2D array

grid = [r1,r2,r3,r4,r5,r6,r7,r8,r9]

if len(grid) != 9 or len(grid[0]) != 9:
    print("There is an error present within your puzzle. Please try again.")


# Runs the main program
if(Solve(grid)): 
     DisplayGrid(grid)
else: 
    print ("There is no solution to this puzzle, or this program cannot solve this program. Please make sure you entered the correct values")
  
