import math


def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(map(int,f.read().split('\n')))
  return data

def count_ThreeWinSum_increase():

  data = read_data()
  count = 0  
  win_start = 0
  win_end = win_start + 2
  last_win_sum = math.inf

  while win_end <= len(data):             
        win_sum = sum(data[win_start:win_end+1])      
        if win_sum > last_win_sum:
          count+=1
        win_start+=1
        win_end = win_start + 2
        last_win_sum=win_sum

  return count      


def main():
  print(count_ThreeWinSum_increase())

if __name__ == "__main__":
  main()  