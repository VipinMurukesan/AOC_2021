def read_data(file = "data.txt",sep=","):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data
 

def counter(age,count_map):
  count = 0
  if age in count_map:
     return count_map[age]
  if age >= 0:
     count = 1
  else:
  # -1 age means a fish with age 6 and a new fish with age 8
    count= counter(age+7,count_map) + counter(age+9,count_map) 
  count_map[age] = count
  return count


def get_fish_count(days=0):
  fishes = []
  for age in read_data():
    fishes.append(int(age))

  fish_count = 0
  count_map = {}
  for fish_age in fishes:
    fish_count += counter(fish_age-days,count_map)
  print(f"After {days} days fish count will be {fish_count}") 


def main():  
  get_fish_count(days=256)

if __name__ == "__main__":
  main()  