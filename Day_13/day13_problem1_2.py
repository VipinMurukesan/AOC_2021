import os 
import re


def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split('\n'))
  return data


class Point():

  def __init__(self,coord_x,coord_y):
    self.x,self.y=coord_x,coord_y
    self.mark = 0

  def set_mark(self):
    self.mark += 1

  def get_mark(self):
    return self.mark
  
  def __str__(self):
    if self.mark:
      return "#".center(2," ")
    return ".".center(2," ")


class Grid():

  def __init__(self,coord_start,coord_end):
    self.min_x,self.min_y = coord_start
    self.max_x,self.max_y = coord_end
    self.points = []
    for i in range(self.max_y+1):
      row_points=[]
      for j in range(self.max_x+1):
        row_points.append(Point(i,j))
      self.points.append(row_points)

  def mark(self,x,y):
    self.points[y][x].set_mark()


  def fold_x(self,x_val):
    grid = Grid((0,0),(x_val-1,self.max_y))
    for i in range(grid.max_y+1):
      for j in range(grid.max_x+1):
        if self.points[i][j].get_mark() or self.points[i][(2*x_val)-j].get_mark():
          grid.points[i][j].set_mark()
    
    self.min_x,self.min_y = grid.min_x,grid.min_y
    self.max_x,self.max_y = grid.max_x,grid.max_y
    self.points = grid.points 

  def fold_y(self,y_val):
    grid = Grid((0,0),(self.max_x,y_val-1))
    for i in range(grid.max_y+1):
       for j in range(grid.max_x+1):
         if self.points[i][j].get_mark() or self.points[(2*y_val)-i][j].get_mark():
          grid.points[i][j].set_mark()
    
    self.min_x,self.min_y = grid.min_x,grid.min_y
    self.max_x,self.max_y = grid.max_x,grid.max_y
    self.points = grid.points     

   #get grid points with mark_count
  def get_marked_points(self,mark_count=0):
    marked_points = []
    counter = 0
    for i in range(self.max_y+1):
      row_points = self.points[i]
      for point in row_points:
        if point.get_mark():
          marked_points.append(point)   
  
    return len(marked_points)

  def __str__ (self):
    grid_str = "Grid: "+os.linesep+"Min Coord: " +str(self.min_x)+","+str(self.min_y)
    grid_str += os.linesep+"Max Coord: " +str(self.max_x)+","+str(self.max_y)
    for i,row_points in enumerate(self.points):
      grid_str += os.linesep
      for point in row_points:
        grid_str += str(point)
    return grid_str


def set_grid(coords,folds):
  
  grid = Grid((0,0),(1500,1500))
  
 
  for item in coords:
    (x,y) = item
    grid.mark(x,y)

  # print(grid)

  print(f"Marked point count: {grid.get_marked_points()}")

  for fold in folds:
    if fold[0] == 0: #y fold
      grid.fold_y(fold[1])
    elif fold[1] == 0: #x fold
      grid.fold_x(fold[0])  

  print(grid)

  print(f"Marked point count: {grid.get_marked_points()}")



def parse_data(data = read_data()):
  coords= []
  folds=[]
  pattern = re.compile(r'^\d+,\d+$')

  for item in data:
    if bool(pattern.match(item)):
      x_str,y_str = item.split(',')
      x,y = int(x_str),int(y_str)
      coords.append((x,y))
    elif "fold along x=" in item:
      folds.append((int(str.removeprefix(item,"fold along x=")),0))      
    elif "fold along y=" in item:
      folds.append((0,int(str.removeprefix(item,"fold along y=")))) 
  return (coords,folds)

def main():
  coords,folds= parse_data()
  
  #set_grid(coords,[folds[0]]) -- problem 1
  
  # set_grid(coords,folds) -- problem 2
  


if __name__ == "__main__":
  main()  