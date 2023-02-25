from cell import *   #personal file


class Grid:
	def __init__(self, rows, cols, width, height, margin_width, margin_height, cell_size):
		self.cells = []
		self.rows = rows
		self.cols = cols
		self.width = width
		self.height = height
		self.cell_size = cell_size
		
		# creating cells
		for i in range(rows):
			self.cells.append([])
			for j in range(cols):
				self.cells[i].append(Cell(margin_width + cell_size * j, margin_height + cell_size * i))
				
	def draw(self, _canvas):
		# draws actual grid
		for n in range(self.rows - 1):
			_canvas.create_line(self.cells[n][0].x, self.cells[n][0].y + self.cell_size, self.cells[n][0].x + self.width, self.cells[n][0].y + self.cell_size, fill = "#0DA192", width = self.height/(10 * self.rows))
			_canvas.create_line(self.cells[0][n].x + self.cell_size, self.cells[0][n].y, self.cells[0][n].x + self.cell_size, self.cells[0][n].y + self.height, fill = "#0DA192", width = self.height/(10 * self.rows))
		
		# draws cell contents
		for i in range(self.rows):
			for j in range(self.cols):
				currentCell = self.cells[i][j]
				
				currentCellOccupationColor = "black" if currentCell.occupiedBy == 'x' else "#f2EBD3"
				
				_canvas.create_text(currentCell.x + self.cell_size/2, currentCell.y + self.cell_size/2.5, text = currentCell.occupiedBy, fill = currentCellOccupationColor, font = ("Helvetica {} bold".format(int(self.cell_size))))
