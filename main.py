"""
Todo:
1. Take a puzzle and save it in, 3D array?
2. Choose random number that is not in the row and colunm already, move on. 



"""
import sys
sys.setrecursionlimit(15000)
class SudukoSolver(): 
	#INIT Function
	def __init__(self):
		#self.UserInput()
		self.TestInput()
		print(self.Solve())
		if(self.Solve()):
			print(self.Grid)
	#Takes user input of puzzle
	def TestInput(self):
		#self.Grid = [[3,1,8,0,2,0,0,9,0],[0,0,6,0,0,0,0,2,0],[0,2,5,9,0,0,0,0,0],[0,6,0,2,0,0,1,5,0],[2,5,0,7,0,9,0,4,3],[0,9,3,0,0,6,0,8,0],[0,0,0,0,0,5,2,7,0],[0,7,0,0,0,0,4,0,0],[0,8,0,0,1,0,9,3,5]]
		self.Grid = [
		[4,0,2,0,0,5,0,3,0],
		[0,0,0,0,0,9,5,1,0],
		[1,0,5,9,3,0,7,0,0],
		[0,0,0,0,0,9,5,1,0],
		[6,4,0,0,0,0,0,2,3],
		[0,5,3,4,0,0,0,0,0],
		[0,0,6,0,7,3,2,0,9],
		[3,2,4,6,0,0,0,0,0],
		[0,7,0,2,0,0,3,0,8]



		]
		#self.FindEmptyBox()

	def UserInput(self):
		self.r1 =(input("Enter numbers in the first row, if box is blank use 0: "))
		self.r2 =(input("Enter numbers in the second row, if box is blank use 0: "))
		self.r3 =(input("Enter numbers in the third row, if box is blank use 0: "))
		self.r4 =(input("Enter numbers in the fourth row, if box is blank use 0: "))
		self.r5 =(input("Enter numbers in the fith row, if box is blank use 0: "))
		self.r6 =(input("Enter numbers in the sixth row, if box is blank use 0: "))
		self.r7 =(input("Enter numbers in the seventh row, if box is blank use 0: "))
		self.r8 =(input("Enter numbers in the eigth row, if box is blank use 0: "))
		self.r9 =(input("Enter numbers in the ninth row, if box is blank use 0: "))
		#Makes sure all rows are at least 9 numbers long
		if (len(self.r1) and len(self.r2) and len(self.r3) and len(self.r4) and len(self.r5) and len(self.r6) and len(self.r7) and len(self.r8) and len(self.r9) == 9):
			self.ToGrid()
		else:
			print("Not all rows contained nine values, please re-enter the puzzle.")
			self.UserInput()
	#Changes the strings to 
	def ToGrid(self):
		self.r1L = [];self.r2L = [];self.r3L = [];self.r4L = [];self.r5L = [];self.r6L = [];self.r7L = [];self.r8L = [];self.r9L = [];

		for i in range(0,len(self.r1),1):
			self.r1L += (self.r1[i])
			self.r2L += (self.r2[i])
			self.r3L += (self.r3[i])
			self.r4L += (self.r4[i])
			self.r5L += (self.r5[i])
			self.r6L += (self.r6[i])
			self.r7L += (self.r7[i])
			self.r8L += (self.r8[i])
			self.r9L += (self.r9[i])
		self.Grid = [[(self.r1L)],[self.r2L],[self.r3L],[self.r4L],[self.r5L],[self.r6L],[self.r7L],[self.r8L],[self.r9L]]

	"""
	BEGINS SOLVING SUKUKO
	"""
	def FindEmptyBox(self):
		for r in range(9):
			for c in range(9):
				if (self.Grid[r][c]==0):
					#this may need to be changed
					self.r = r
					self.c = c
					self.l[0] = self.r
					self.l[1]= self.c
					return True
		return False
	def InRow(self):
		for i in range(9):
			if(self.Grid[self.r][i]==self.num):
				return True
		return False 

	def InCol(self):
		for i in range(9):
			if(self.Grid[i][self.c]==self.num):
				return True
		return False
	def InBox(self):
		for i in range(3):
			for j in range(3):
				if(self.Grid[i+(self.row-(self.row%3))][j+(self.col - (self.col%3))]== self.num):
					return True
		return False
	def CanNumBePlaced(self):
		return not self.InRow() and not self.InCol() and not self.InBox()


	def Solve(self):
		
		self.Grid = [
		[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]

		]

		
		self.l = [0,0]



		if(not self.FindEmptyBox()):
			return True

		self.row = self.l[0]
		self.col = self.l[1]

		for self.num in range(1,10):
			#print(self.num)
			if(self.CanNumBePlaced()):
				self.Grid[self.row][self.col] = self.num
				if(self.Solve()):
					return True
				self.Grid[self.row][self.col] = 0
		
		return False 

SudukoSolver()
