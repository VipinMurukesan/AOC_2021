def read_data(file = "data.txt",sep=","):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split(sep))
  return data



class LaternFish():
  DEFAULT_AGE = 8
  MAX_AGE = 6
  def __init__(self,age=DEFAULT_AGE):
    self.age = age 

  def __str__(self):
    return str(self.age)

  def get_old(self):

    if self.age == 0:
      return [LaternFish(self.MAX_AGE),LaternFish(self.DEFAULT_AGE)]
   
    self.age -= 1
    return [LaternFish(self.age)] 


def age_fishes(fishes):
    older_fishes = []
    for fish in fishes:
      older_fishes.extend(fish.get_old())
    return older_fishes  


def generate_fishes(days = 0):
  fishes = []
  for age in read_data():
    fishes.append(LaternFish(int(age)))

  print([str(fish) for fish in fishes])

  for day in range(days):
    fishes = age_fishes(fishes) 
    print([str(fish) for fish in fishes])

  print(f"Count of fishes after {days} days: {len(fishes)} ")  

def main():
  generate_fishes(100)


if __name__ == "__main__":
  main()