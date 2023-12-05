
def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split('\n'))
  return data


class Bingo:
  rows, cols = (5, 5)

  def __init__(self,bingo_fields):
    self.values = [[0 for i in range(self.cols)] for j in range(self.rows)]
    self.last_mark = -1
    self.won = False
    for i in range(self.rows):
      row_values = bingo_fields[i].split()
      for j in range(self.cols):
        self.values[i][j] = int(row_values[j])
    # print(self.values)    

  def mark(self,value):
    self.last_mark = value
    for i in range(self.rows):
      for j in range(self.cols):
        if self.values[i][j] == value:
          self.values[i][j] = -1 #indicate the value is marked
          return

  def win_status(self):     
    for i in range(self.rows):  
        row_value = self.values[i]    
        row_match = all(x== -1 for x in row_value)
        if row_match:
          self.won = True
          return self.won
    for i in range(self.rows):
      col_value = []
      for j in range(self.cols):
        col_value.append(self.values[j][i])        
      col_match = all(x== -1 for x in col_value)
      if col_match:
        self.won = True
        return self.won    
    return self.won
  
  def score(self):    
    if(self.won):
      sum_unmarked = 0
      for i in range(self.rows):  
        row_value = self.values[i]
        row_sum = sum([value for value in row_value if value != -1])
        sum_unmarked += row_sum
      score = self.last_mark * sum_unmarked
      return score  

  def __str__(self):
    return(str(self.values))      


def losers_bingo(data=read_data()):
  bingo_calls = [int(value) for value in data.pop(0).split(',')]  
  bingo_values = [value for value in data if value != '' ]

  bingos = []  
  bingo_count = (len(bingo_values)//Bingo.rows)

  for count in range(bingo_count):
    bingos.append(Bingo(bingo_values[count*Bingo.rows:(count*Bingo.rows)+Bingo.rows]))

  #remove winning bingos one by one from game till the last remaining one to pick
  playing_bingos = list(range(bingo_count))
  

  for call_index,call in enumerate(bingo_calls):
    round_winners = []
    for bingo_index in playing_bingos:
      bingo = bingos[bingo_index]
      bingo.mark(call)
      if bingo.win_status():
        if len(playing_bingos) == 1:
          print("Last Bingo Won! Winning Index: ",bingo_index+1)
          score = bingo.score()
          print(score)
          return
        else:
          round_winners.append(bingo_index)
    # print(round_winners)      
    playing_bingos = [ item for item in playing_bingos if item not in round_winners] 
  

def main():
  losers_bingo()

if __name__ == "__main__":
  main()  