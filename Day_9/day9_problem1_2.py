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
    return neighbour_indices 


  def get_low_points(self):
    low_points=[]

    def is_localminimum(value,neighbour_indices):
      neigbour_values = []
      for (row_index,col_index) in neighbour_indices:
        neigbour_values.append(self.elements[row_index][col_index])
      return all(value<n_value for n_value in neigbour_values)  
    
    for row in range(self.row_count):
      for col in range(self.col_count):
        point_value = (self.elements[row][col])
        neighbours = self.get_neighbour_indices(row,col)
        if(is_localminimum(point_value,neighbours)):
          low_points.append((row,col))
    
    return low_points      
     


  def get_basins(self,row,col,basins=[],visited=[]):
    if self.elements[row][col] < 9:
      basins.append(self.elements[row][col])
      visited.append((row,col))

      neighbour_indices = self.get_neighbour_indices(row,col)
      for (n_row,n_column) in neighbour_indices:
        if (n_row,n_column) not in visited:
          self.get_basins(n_row,n_column,basins,visited)


  def get_risk_levels(self):
    risk_level=0
    low_points = self.get_low_points()    
    for (row,col) in low_points:
      risk_level += (self.elements[row][col]+1)
    return risk_level  

  def get_top_three_basin_product(self):
    basin_lengths =[]
    low_points = self.get_low_points()    
    for (row,col) in low_points:
      basins = []
      self.get_basins(row,col,basins)
      basin_lengths.append(len(basins))
    basin_lengths.sort(reverse=True)
    # print(basin_lengths)
    return basin_lengths[0] * basin_lengths[1] *basin_lengths[2]

      

  def __str__(self):
    return f"Grid Row-Count: {self.row_count} Column-Count: {self.col_count}"    

def main():
  grid = Grid()
  print(grid.get_risk_levels())
  print(grid.get_top_three_basin_product())


if __name__ == "__main__":
  main()