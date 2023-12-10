import math

def read_data(file = "data.txt",sep=","):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data


def brute_force(numbers):
  min_num = min(numbers)
  max_num = max(numbers)

  min_cost = math.inf

  for dest in range(min_num,max_num+1):
    cost = 0
    for num in numbers:
      steps = abs(dest-num)
      cost += (steps*(steps+1)/2)
    if cost < min_cost:
      min_cost = cost
  return min_cost




def calculate_fuel(data=read_data()):
  positions = [int(item) for item in data]
  print(brute_force(positions))




def main():
  print(calculate_fuel())

if __name__ == "__main__":
  main()  