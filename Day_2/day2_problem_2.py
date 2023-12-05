from enum import StrEnum

def read_data(file = "data.txt"):
  data=[]
  with open(file,'r') as f:
    data = list(f.read().split('\n'))
  return data

class Direction(StrEnum):
  FORWARD = 'forward'
  DOWN = 'down'
  UP = 'up'


def get_final_location(data=read_data()):
  vertical = 0
  horizontal = 0
  aim = 0
  for inst in data:
    dirn,dist = inst.split(' ')
    # print(dirn,dist)
    if dirn == Direction.FORWARD:
      horizontal += int(dist)
      vertical += (aim*int(dist))
    elif dirn== Direction.UP:
      aim -= int(dist)
    elif dirn == Direction.DOWN:
      aim += int(dist)  
  return (vertical,horizontal)      

def main():
  vertical,horizontal = get_final_location()
  print(vertical*horizontal)

if __name__ == "__main__":
  main()  