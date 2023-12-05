
def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(map(int,f.read().split('\n')))
  return data


def count_increase():
  data = read_data()
  count = 0
  for i in range(1,len(data)):
    if data[i-1]<data[i]:
      count +=1
  return count    


def main():
  print(count_increase())

if __name__ == "__main__":
  main()  