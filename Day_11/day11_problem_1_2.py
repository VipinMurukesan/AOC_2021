import os


def read_data(file = "data.txt",sep="\n"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data

class Grid():

  def __init__(self,rows = read_data()):
    self.elements = []
    for row in rows:
      current_row = []
      for el in row:
        current_row.append(int(el)) 
      self.elements.append(current_row)
    self.row_count = len(self.elements)
    self.col_count = len(self.elements[0])

  def get_neighbour_indices(self,row,col):
    neighbour_indices = []
    if row-1 >= 0:
      neighbour_indices.append((row-1,col))
    if row+1 < self.row_count:
      neighbour_indices.append((row+1,col))
    if col-1 >= 0:
      neighbour_indices.append((row,col-1))
    if col+1 < self.col_count:
      neighbour_indices.append((row,col+1))
    if row-1 >= 0 and col-1 >= 0:
      neighbour_indices.append((row-1,col-1))
    if row+1 < self.row_count and col+1 < self.row_count:
      neighbour_indices.append((row+1,col+1))
    if row-1 >= 0 and col+1 < self.row_count:
      neighbour_indices.append((row-1,col+1))
    if row+1 < self.row_count and col-1 >= 0:
      neighbour_indices.append((row+1,col-1))                
    return neighbour_indices      


  def update_neighbours(self,row,column):
    neighbour_indices=self.get_neighbour_indices(row,column)
    for (row,column) in neighbour_indices:
      if self.elements[row][column] <= 9:
        self.elements[row][column] += 1
        if self.elements[row][column] == 10:
          self.update_neighbours(row,column)


  
  def update_step(self,steps):
    total_flashes = 0

    for _ in range(steps):
      to_flash = []          
      for row in range(self.row_count):
        for column in range(self.col_count):
          self.elements[row][column] += 1
          if self.elements[row][column] > 9:
            to_flash.append((row,column))
      for (row,column) in to_flash:
        self.update_neighbours(row,column)
      total_flashes += self.update_flash()

    return total_flashes  

  def update_flash(self):
    flash = 0
    for row in range(self.row_count):
      for column in range(self.col_count):
        if self.elements[row][column] > 9:
          self.elements[row][column] = 0
          flash += 1
    return flash      
       
  def __str__(self):
    pattern =""
    for row in range(self.row_count):
      for column in range(self.col_count):
        pattern += f"{str(self.elements[row][column]):^4}"
      pattern += os.linesep 
    return pattern   



def main():
  grid = Grid(read_data())
  # print(grid)
  steps = 100 
  flashes = grid.update_step(steps)
  print(grid)
  print(f"Total flashes after {steps} = {flashes}")

  grid = Grid(read_data())
  steps = 0
  
  while flashes != grid.row_count *grid.col_count:
    steps += 1
    flashes = grid.update_step(1)

  print(grid)
  print(f"Synchronized flashes after {steps}")


if __name__ == "__main__":
  main()

