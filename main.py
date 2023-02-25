from tkinter import *
from grid import *  #personal file


# grid dimensions
rows_and_cols = 3

#window dimensions
window_width = 600
window_height = 600

#grid dimensions
grid_width = window_width/1.5
grid_height = window_height/1.5

cell_size = grid_width/rows_and_cols

players = ['x', 'o']
turn = players[0]

gameOver = False
tie = False
winner = ''

canvas_bg = "#18BCAC"



grid = Grid(rows_and_cols, rows_and_cols, grid_width, grid_height, (window_width-grid_width) / 2, (window_height-grid_height) / 2, cell_size) #creating a grid object



root = Tk() # root tkinter window
root.title("Tic Tac Toe") #title of game
root.geometry("{0}x{1}".format(window_width, window_height)) #setting the window dimensions
root.resizable(False, False) #disabling user's window resizing ability


# callback function for clicking mouse on canvas
def mouseClicked(event):
	global turn, gameOver
	
	for i in range(rows_and_cols):
		for j in range(rows_and_cols):
			if (event.x >= grid.cells[i][j].x and event.x <= grid.cells[i][j].x + cell_size and event.y >= grid.cells[i][j].y and event.y <= grid.cells[i][j].y + cell_size) and not gameOver:
				if grid.cells[i][j].occupiedBy == '':
					grid.cells[i][j].occupiedBy = turn
					turn = players[abs(players.index(turn) - 1)]
								
					grid.draw(canvas)
					checkIfGameOver()
				else:
					print("Occupied cell!")
				
				whenGameOver()


canvas = Canvas(root, bg = canvas_bg, height = window_width, width = window_height)
canvas.bind("<Button-1>", mouseClicked)

grid.draw(canvas)



def checkIfWin():
	global winner, gameOver
	
	
	rows_filled = list(set((grid.cells[i][j].occupiedBy == grid.cells[i][0].occupiedBy) and grid.cells[i][j].occupiedBy != '' for j in range(rows_and_cols)) for i in range(rows_and_cols))
	cols_filled = list(set((grid.cells[j][i].occupiedBy == grid.cells[0][i].occupiedBy) and grid.cells[j][i].occupiedBy != '' for j in range(rows_and_cols)) for i in range(rows_and_cols))
	
	# horizontal in a row
	if set([True]) in rows_filled:
		winner = grid.cells[rows_filled.index(set([True]))][0].occupiedBy
		gameOver = True
	
	# vertical in a row
	elif set([True]) in cols_filled:
		winner = grid.cells[0][cols_filled.index(set([True]))].occupiedBy
		gameOver = True
	
	# diagonal (left to right) in a row
	elif all((grid.cells[i][i].occupiedBy == grid.cells[0][0].occupiedBy) and grid.cells[i][i].occupiedBy != '' for i in range(rows_and_cols)):
		winner = grid.cells[0][0].occupiedBy
		gameOver = True
		
	# diagonal (right to left) in a row
	elif all((grid.cells[i][rows_and_cols - 1 - i].occupiedBy == grid.cells[0][rows_and_cols - 1].occupiedBy) and grid.cells[i][rows_and_cols - 1 - i].occupiedBy != '' for i in range(rows_and_cols)):
		winner = grid.cells[0][rows_and_cols - 1].occupiedBy
		gameOver = True


def checkIfTie():
	global gameOver, tie
	
	# if all the cells are not empty, ultimately all being filled, and there is no winner, then it is a tie.
	if all(sum(list(list(cell.occupiedBy != '' for cell in row) for row in grid.cells), [])) and winner == '':
		tie = True
		gameOver = True
	

def checkIfGameOver():
	checkIfWin() #first, check if win
	checkIfTie() #if not, then check if tie


def whenGameOver():
	global canvas
	
	if gameOver:
		if tie:
			print("Tie")
			canvas.create_text(window_width/2, (window_height - grid_height)/4, text = "Tie", font = ("Helvetica {} bold".format(int(cell_size/2))))
		else:
			print("Winner is: {}".format(winner))
			canvas.create_text(window_width/2, (window_height - grid_height)/4, text = winner + " wins", font = ("Helvetica {} bold".format(int(cell_size/2))))



canvas.pack()
root.mainloop()
