import os

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
      return str(self.mark).center(4," ")
    return "*".center(4," ")



class Grid():

  def __init__(self,coord_start,coord_end):
    self.min_x,self.min_y = coord_start
    self.max_x,self.max_y = coord_end
    self.points = []
    for i in range(self.max_x+1):
      row_points=[]
      for j in range(self.max_y+1):
        row_points.append(Point(j,i))
      self.points.append(row_points)


  def mark_hline(self,x_start,x_end,y):
    row_points = self.points[y]
    for i in range(x_start,x_end+1):
      row_points[i].set_mark()

  def mark_vline(self,y_start,y_end,x):
    for i in range(y_start,y_end+1):
      (self.points[i])[x].set_mark()

  def mark_dline(self,x_start,y_start,x_end,y_end):
    slope = int((y_end-y_start)/(x_end-x_start))
    coords_on_line = [(x_start,y_start)]
    while x_start != x_end:
      x_start += 1
      y_start += slope
      coords_on_line.append((x_start,y_start))    
    for coord in coords_on_line:
      #reuse the existing methods to do individual point marking
      #line starting and ending at same point
      self.mark_vline(coord[1],coord[1],coord[0])    
        

  def mark_line(self,line_start_coord,line_end_coord):
    line_start_x,line_start_y=line_start_coord
    line_end_x,line_end_y = line_end_coord

    #vertical lines
    if(line_start_x == line_end_x):
      if line_start_y > line_end_y:
         line_start_y,line_end_y =line_end_y,line_start_y
      self.mark_vline(line_start_y,line_end_y,line_start_x)

    #horizontal lines
    elif(line_start_y == line_end_y):
      if line_start_x>line_end_x:
        line_start_x,line_end_x = line_end_x,line_start_x
      self.mark_hline(line_start_x,line_end_x,line_start_y)

    #other lines are diagonal lines (mentioned in problem statement)
    elif(abs((line_end_y-line_start_y)/(line_end_x-line_start_x)) == 1):
      if line_start_x>line_end_x:
        line_start_x,line_end_x = line_end_x,line_start_x
        line_start_y,line_end_y = line_end_y,line_start_y      

      #print("Diagonal line between ",line_start_x,line_start_y,line_end_x,line_end_y)
      self.mark_dline(line_start_x,line_start_y,line_end_x,line_end_y)
  

  #get grid points with mark_count
  def get_marked_points(self,mark_count=0):
    marked_points = []
    counter = 0
    for i in range(self.max_x+1):
      row_points = self.points[i]
      for point in row_points:
        if point.get_mark() >= mark_count:
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


def set_grid(data = read_data()):
  
  grid = Grid((0,0),(1000,1000))
  #print(grid)
  
  
  for item in data:
    str1,str2 = item.split('->')
    x_start,y_start = str1.split(',')
    x_end,y_end = str2.split(',') 
    x_start,y_start,x_end,y_end = int(x_start),int(y_start),int(x_end),int(y_end)    
    grid.mark_line((x_start,y_start),(x_end,y_end))

  #print(grid)

  print("Grid Count > 2 : ", grid.get_marked_points(2))



def main():
  set_grid()
  


if __name__ == "__main__":
  main()  